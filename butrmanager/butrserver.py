import logging

from server.config import CONFIG
from server.service import Service

logger = logging.getLogger('butrserver')


if __name__ == '__main__':
    logger.info('Initializing service instance')
    instance = Service(CONFIG.mode, CONFIG.port, CONFIG.password)
    logger.info('Starting service')
    instance.run_forever()
