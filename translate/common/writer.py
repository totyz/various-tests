import abc
import logging
from pathlib import Path
from typing import List, Tuple, Union

from .common import setup_logger, KeyValue
from .paths import OUTPUTS_PATH


class Writer(abc.ABC):
    def __init__(self, fn_out: str):
        self.logger = setup_logger('writer', logging.DEBUG)
        self._fn_out = OUTPUTS_PATH / fn_out
        self._fd = None
        if self._fn_out.exists():
            raise IOError(f"{self._fn_out} exists")

    @property
    def output_file(self):
        return self._fn_out

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

    def write(self, data: Union[List[KeyValue], Tuple]):
        if isinstance(data, KeyValue):
            data = [data]
        [self._fd.write('K:' + el.key + '\n' + 'V:' + el.value + '\n') for el in data]


class BinWriter(Writer):
    def open(self):
        self._fd = open(self._fn_out, mode='wb')
        return self._fd

    def close(self):
        self._fd.close()

    def write(self, data: Union[List[KeyValue], Tuple]):
        if isinstance(data, KeyValue):
            data = [data]
        [self._fd.write(('#' + el.key + ':' + el.value).encode('UTF-8')) for el in data]


class WriterFactory:
    @staticmethod
    def create(writer_type):
        writers = {
            'txt': TxtWriter,
            'bin': BinWriter,
        }
        if writer_type not in writers:
            raise ValueError(f"Reader '{writer_type}' is not supported yet")
        return writers[writer_type]