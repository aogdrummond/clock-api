import logging
import logging.config

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "consoleFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "fileFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "consoleFormatter",
            "stream": "ext://sys.stdout"
        },
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "fileFormatter",
            "filename": "logs/app.log"
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["consoleHandler"]
        },
        "appLogger": {
            "level": "DEBUG",
            "handlers": ["fileHandler"],
            "qualname": "appLogger",
            "propagate": 0
        }
    }
}

def setup_logging(config_dict:dict):

    logging.config.dictConfig(config_dict)