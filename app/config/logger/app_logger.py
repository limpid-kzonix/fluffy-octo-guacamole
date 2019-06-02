import logging
import sys

LOGGING_CONFIG_SERVER = dict(
    version=1,
    disable_existing_loggers=False,
    loggers={
        "app.info": {
            "level": "INFO",
            "handlers": ["access_console"],
            "propagate": True,
            "qualname": "app.info",
        },
        "app.debug": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": True,
            "qualname": "app.debug",
        },
        "app.warning": {
            "level": "WARNING",
            "handlers": ["access_console"],
            "propagate": True,
            "qualname": "APP.WARN",
        },
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout,
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stderr,
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": sys.stdout,
        },
    },
    formatters={
        "generic": {
            "format": "%(asctime)s : PID=[%(process)d] : [%(levelname)s] - %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(method_name)s]: "
                      + "%(status)s - %(message)s ",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        },
    },
)

app_logger = logging.getLogger("app.info")
logger = logging.getLogger("app.debug")
error_logger = logging.getLogger("app.warning")
