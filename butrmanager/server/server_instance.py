from subprocess import Popen, PIPE, DEVNULL, TimeoutExpired
import logging
import os

import psutil

from .config import APP_PATH

logger = logging.getLogger('instance')


def is_running(pid):
    """Check if pid is alive"""
    try:
        psutil.Process(pid)
        return True
    except psutil.error.NoSuchProcess:
        return False


class ServerInstance:
    """Manages a minecraft server instance"""
    def __init__(self, name, config):
        logger.debug('Initializing {} from: {}'.format(name, config))
        self.name = name
        self.folder = os.path.join(APP_PATH, config['folder'])
        self.alive = False
        self.process = None

        self.run_command = [
            'java',
            '-Xmx{}M'.format(config['memory']),
            '-jar',
            config['jar'],
        ]
        if 'args' in config:
            self.run_command.extend(config['args'])

    def start(self):
        """Starts the server process."""
        logger.info('Starting {} in {}'.format(self.name, self.folder))
        try:
            logger.debug('Executing {}'.format(self.run_command))
            self.process = Popen(
                self.run_command,
                stdin=PIPE,
                stdout=DEVNULL,
                stderr=DEVNULL,
                cwd=self.folder,
            )
        except:
            logger.exception('Error when starting {}'.format(self.name))
            return False

        if is_running(self.process.pid):
            logger.info('Started {}'.format(self.name))
            self.alive = True
            return True
        else:
            logger.error('Failed to start {}'.format(self.name))
            return False

    def stop(self):
        """Gracefully stops the server process."""
        logger.info('Stopping {}'.format(self.name))
        try:
            self.process.stdin.write('stop\n'.encode('utf-8'))
            self.process.stdin.flush()
        except:
            logger.exception('Error writing to server input')

        try:
            self.process.wait(timeout=10)
        except TimeoutExpired:
            logger.error('Failed to stop {}'.format(self.name))
            return False

        logger.info('Stopped {}'.format(self.name))
        self.alive = False
        return True

    def send_command(self, command):
        """Sends a command to the server process."""
        logger.info('Sending command {} to {}'.format(command, self.name))
        parts = command.split(' ')
        parts[0] = parts[0].lower()
        if parts[0] == 'stop':
            return False
        command = ' '.join(parts)
        try:
            self.process.stdin.write('{}\n'.format(command).encode('utf-8'))
            self.process.stdin.flush()
        except:
            logger.exception('Error writing to server input')
            return False
        return True

    def read_log(self, lines=10):
        """Returns n lines from end of log file, defaults to 10."""
        raise NotImplementedError('Reading from log file not yet implemented')

    def get_memory_usage(self):
        """Return RSS memory used in MB."""
        logger.info('Getting memory usage of {}'.format(self.name))
        process = psutil.Process(self.process.pid)
        memory_used = (process.memory_info().rss / 1024) / 1024
        return memory_used
