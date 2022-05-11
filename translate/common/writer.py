import abc
import logging
from pathlib import Path
from typing import List

from .common import setup_logger
from .paths import OUTPUTS_PATH


class Writer(abc.ABC):
    def __init__(self, fn_out: str):
        self.logger = setup_logger('writer', logging.DEBUG)
        self._fn_out = OUTPUTS_PATH / fn_out
        self._fd = None
        if self._fn_out.exists():
            raise IOError(f"{self._fn_out} exists")

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def write(self, data: List):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class TxtWriter(Writer):

    def open(self):
        self._fd = open(self._fn_out, mode='w')
        return self._fd

    def close(self):
        self._fd.close()

    def write(self, data: List):
        for el in data:
            key, value = el
            self._fd.write('K:' + key + '\n')
            self._fd.write('V:' + value + '\n')
        # for_test - change it into list comprehension


class BinWriter(Writer):
    pass


class WriterFactory:
    @staticmethod
    def create(writer_type):
        writers = {
            'txt': TxtWriter,
        }
        return writers[writer_type]