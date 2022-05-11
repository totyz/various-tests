import argparse

from common.paths import INPUTS_PATH
from common.reader import ReaderFactory
from common.writer import WriterFactory

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True,
                        help="Pass input file from inputs folder")
    parser.add_argument("--output", required=False,
                        help="Save data to output folder to selected output file")
    args = parser.parse_args()

    reader = ReaderFactory().create(args.input.split('.')[-1])
    writer = WriterFactory().create(args.output.split('.')[-1])
    with reader('input.txt') as rr, writer(args.output) as ww:
            ww.write(rr.read_all())
