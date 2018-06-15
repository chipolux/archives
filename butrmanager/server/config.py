from logging.config import dictConfig
import json
import os
import sys


APP_PATH = os.path.dirname(__file__)
DEFAULT_LOG_FILE = os.path.join(APP_PATH, 'butrserver.log')


class FileBasedConfig(object):
    def __init__(self, path, defaults):
        self.path = path
        self.defaults = defaults
        self.load()

    def load(self):
        if os.path.isfile(self.path):
            with open(self.path, 'r') as f:
                config = json.load(f)
        else:
            config = {}

        for key, value in config.items():
            setattr(self, key, value)

    def to_dict(self):
        config = {}
        for key, value in self.__dict__.items():
            if key in ['path', 'defaults']:
                continue
            config[key] = value

        return config

    def save(self):
        config = self.to_dict()
        with open(self.path, 'w') as f:
            json.dump(config, f, indent=4, separators=(',', ': '))

    def __getattr__(self, name):
        return self.defaults.get(name, None)


CONFIG = FileBasedConfig(
    os.path.join(APP_PATH, 'config.json'),
    {
        "console_log_level": "INFO",
        "file_log_level": "ERROR",
        "file_log_path": DEFAULT_LOG_FILE,
        "mode": "local",
        "port": 31337,
        "servers": {},
    },
)

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s [%(process)d] %(levelname)-8s %(name)s: %(message)s'  # noqa
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'detailed',
            'level': CONFIG.console_log_level
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': CONFIG.file_log_path,
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'detailed',
            'level': CONFIG.file_log_level
        },
        'null': {'class': 'logging.NullHandler'}
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}
LOG_DIR = os.path.dirname(LOGGING['handlers']['file']['filename'])
os.makedirs(LOG_DIR, exist_ok=True)
dictConfig(LOGGING)
