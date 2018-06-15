import logging
import queue

from .config import CONFIG
from .server_instance import ServerInstance
from .socket_server import SocketServer

logger = logging.getLogger('service')


class Service:
    """Service that brokers communication between servers and instances"""
    def __init__(self, mode, port, password, as_win_service=False):
        self.mode = mode
        self.port = port
        self.password = password
        self.as_win_service = as_win_service
        self.shutdown_requested = False

        self.instances = {}
        self.processing_queue = queue.Queue(15)
        self.response_queue = queue.Queue(15)

        if self.mode == 'local':
            logger.info('Binding to localhost')
            self.hostname = 'localhost'
        elif self.mode == 'remote':
            logger.info('Binding to 0.0.0.0')
            self.hostname = '0.0.0.0'
        else:
            logger.info('Invalid mode setting, binding to localhost')
            self.hostname = 'localhost'

        self.setup_socket_server()

    def setup_socket_server(self):
        logger.info('Setting up socket server')
        self.socket_server = SocketServer(
            self.hostname,
            self.port,
            self.processing_queue,
            self.response_queue,
        )
        self.socket_server.start()

    def run_forever(self):
        try:
            while not self.shutdown_requested:
                self.run_once()
        except KeyboardInterrupt:
            logger.info('Shutting down service')
            self.shutdown()

    def run_once(self):
        try:
            msg = self.processing_queue.get(timeout=1)
        except queue.Empty:
            pass
        else:
            if self.is_valid_message(msg):
                self.process_message(msg)
            else:
                self.response_queue.put([msg[0], 'print', 'Bad request'])

            self.processing_queue.task_done()

    def is_valid_message(self, msg):
        # msg should be [id, command, opt-instance, opt-args, opt-password]
        if len(msg) < 2:
            logger.debug('Invalid message length: {}'.format(msg))
            return False

        # provided password should match config if set
        if self.password:
            if msg[-1] != self.password:
                logger.debug('Invalid password: {}'.format(msg))
                return False
            else:
                msg.remove(self.password)

        return True

    def process_message(self, msg):  # noqa
        msg_id = msg.pop(0)
        command = msg.pop(0).lower()

        if command in ['start', 'stop', 'memory', 'command']:
            try:
                instance = msg.pop(0)
            except IndexError:
                command = None
                resp = ['print', 'Command requires server name']

        if command == 'start':
            resp = self.start_instance(instance)
        elif command == 'stop':
            resp = self.stop_instance(instance)
        elif command == 'memory':
            resp = self.memory_instance(instance)
        elif command == 'command':
            try:
                command = msg.pop(0)
            except:
                resp = ['print', 'Must provide command to run on server']
            else:
                resp = self.command_instance(instance, command)
        elif command == 'list':
            resp = self.list_all_instances()
        elif command == 'online':
            resp = self.list_online_instances()
        elif command == 'shutdown':
            resp = self.shutdown()

        resp.insert(0, msg_id)
        logger.debug('Response {}'.format(resp))
        self.response_queue.put(resp)

    def start_instance(self, instance):
        logger.debug('Start requested for {}'.format(instance))
        if instance in self.instances:
            server = self.instances[instance]
        else:
            config = CONFIG.servers.get(instance)
            if config is None:
                return ['print', 'No server with that name']
            try:
                server = ServerInstance(instance, config)
                self.instances[instance] = server
            except:
                return ['print', 'Failed to initialize server']

        if server.alive:
            return ['print', 'Server already running']
        else:
            result = server.start()
            return ['print', 'Start status: {}'.format(result)]

    def stop_instance(self, instance):
        logger.debug('Stop requested for {}'.format(instance))
        if instance not in self.instances:
            return ['print', 'Server never started']

        server = self.instances[instance]
        if server.alive:
            result = server.stop()
            return ['print', 'Stop result: {}'.format(result)]
        else:
            return ['print', 'Server not running']

    def memory_instance(self, instance):
        logger.debug('Memory report requested for {}'.format(instance))
        if instance not in self.instances:
            return ['print', 'Server never started']

        server = self.instances[instance]
        if server.alive:
            result = server.get_memory_usage()
            return ['print', 'Memory usage: {}'.format(result)]
        else:
            return ['print', 'Server not running']

    def command_instance(self, instance, command):
        logger.debug('Send command requested for {}'.format(instance))
        if instance not in self.instances:
            return ['print', 'Server never started']

        server = self.instances[instance]
        if server.alive:
            result = server.send_command(command)
            return ['print', 'Command result: {}'.format(result)]
        else:
            return ['print', 'Server not running']

    def list_all_instances(self):
        logger.debug('List of all servers requested')
        servers = list(CONFIG.servers)
        return ['print', servers]

    def list_online_instances(self):
        logger.debug('List of online servers requested')
        online = [k for k, v in self.instances.items() if v.alive]
        return ['print', online]

    def shutdown(self):
        logger.debug('Shutdown requested')
        online = [v for k, v in self.instances.items() if v.alive]
        for server in online:
            logger.debug('Stopping {}'.format(server.name))
            server.stop()

        online = [v for k, v in self.instances.items() if v.alive]
        if len(online) > 0:
            logger.debug('Still online {}'.format(online))
            return ['print', 'Unable to stop all servers, shutdown manually']
        else:
            self.socket_server.shutdown.set()
            self.shutdown_requested = True
            return ['print', 'Stopped all servers, shutting down']


if __name__ == '__main__':
    logger.info('Initializing service instance')
    instance = Service(CONFIG.mode, CONFIG.port, CONFIG.password)
    logger.info('Starting service')
    instance.run_forever()
