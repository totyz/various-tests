import logging
from functools import wraps
from typing import NamedTuple


class KeyValue(NamedTuple):
    key: str
    value: str


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    loggerFormat = "[%(levelname)8s : %(name)2s]\t%(asctime)s:\t%(message)s"
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(CustomFormatter(loggerFormat))
    logger.addHandler(stdout_handler)
    return logger


def lower_case(cmd):
    @wraps(cmd)
    def inner(*args, **kwargs):
        for el in cmd(*args, **kwargs):
            yield KeyValue(el.key, el.value.lower())
    return inner
