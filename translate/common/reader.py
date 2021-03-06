import abc
import logging
from pathlib import Path
from typing import io, Tuple, List

from .common import setup_logger
from .paths import INPUTS_PATH


class Reader(abc.ABC):
    def __init__(self, fn: str):
        self.logger = setup_logger('reader', logging.INFO)
        self._fd = None
        self._fn = INPUTS_PATH / fn

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def read_element(self):
        # generator
        pass

    def read_all(self) -> List[Tuple]:
        return [pair for pair in self.read_element()]

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class TxtReader(Reader):

    def open(self):
        self._fd = open(self._fn)
        return self._fd

    def close(self):
        self._fd.close()

    def read_element() -> Tuple:
        self._fd.seek(0)
        while lineK := self._fd.readline():
            if lineK.startswith('K:'):
                lineV: str = self._fd.readline()
                yield lineK[2:], lineV[2:]


class BinReader(Reader):
    def open(self):
        self._fd = open(self._fn, mode='rb')
        return self._fd

    def close(self):
        self._fd.close()

    def read_element(self):
        self._fd.seek(0)
        found = False
        while c := self._fd.read(1):
            if c == b'#':  # K: starts
                key = b''
                while k := self._fd.read(1):  # for_test - how to normalize, make the method more readable
                    if k == b':':
                        break
                    key += k
                value = b''
                while v := self._fd.read(1):
                    if v == b'#':
                        break
                    value += v
                self._fd.seek(-1, 1)
                found = True
            if found:
                found = False
                yield key.decode('utf-8'), value.decode('utf-8')


class ReaderFactory:
    @staticmethod
    def create(reader_type):
        readers = {
            'txt': TxtReader,
            'bin': BinReader,
        }
        return readers[reader_type]
