import json
import logging
import socket
import threading
import uuid

logger = logging.getLogger('socket')


class SocketServer(threading.Thread):
    """Thread that manages socket communications with the queues"""
    def __init__(self, host, port, processing_queue, response_queue):
        super().__init__()
        logger.debug('Initializing socket server {}:{}'.format(host, port))
        self.shutdown = threading.Event()
        self.processing_queue = processing_queue
        self.response_queue = response_queue
        self.socket = socket.socket()
        self.socket.bind((host, port))
        self.socket.settimeout(0.5)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.listen(5)
        self.workers = []

    def run(self):
        logger.info('Socket server starting')
        while not self.shutdown.is_set():
            try:
                conn, addr = self.socket.accept()
                logger.info('Connection from {}:{}'.format(*addr))
            except socket.timeout:
                pass
            else:
                logger.debug('Initializing worker')
                worker = threading.Thread(
                    target=self.handle_connection, args=(conn, addr)
                )
                worker.start()
                self.workers.append(worker)
                logger.info('Worker started')
            finally:
                # Only keep references to living workers
                worker_count = len(self.workers)
                self.workers = self.get_living_workers()
                if worker_count != len(self.workers):
                    logger.debug('Cleaned dead workers')

        logger.info('Socket server shutting down')
        if len(self.get_living_workers()):
            logger.info('Waiting for workers to die')
            while len(self.get_living_workers()) > 0:
                continue

    def get_living_workers(self):
        return list(filter(lambda x: x.is_alive(), self.workers))

    def handle_connection(self, conn, addr):
        data = conn.recv(8192)
        logger.debug('Recieved {} from {}:{}'.format(data, *addr))

        if data:
            # Add identifier to msg and insert into queue for processing
            data = json.loads(data.decode('utf-8'))
            msg_id = uuid.uuid4()
            data.insert(0, msg_id)
            logger.debug('Inserting msg {} for {}:{}'.format(msg_id, *addr))
            self.processing_queue.put(data)

            # Watch response queue for a response to our msg
            while True:
                msg = self.response_queue.get()
                if msg[0] == msg_id:
                    logger.debug('Recieved response for {}:{}'.format(*addr))
                    break
                else:
                    self.response_queue.task_done()
                    self.response_queue.put(msg)

            msg.remove(msg_id)
            data = json.dumps(msg)
            logger.debug('Sending {} to {}:{}'.format(data, *addr))
            conn.send(data.encode('utf-8'))
            self.response_queue.task_done()

        logger.debug('Closing connection to {}:{}'.format(*addr))
        conn.close()
