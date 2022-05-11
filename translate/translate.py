from common.paths import INPUTS_PATH
from common.reader import ReaderFactory
from common.writer import WriterFactory

if __name__ == '__main__':
    # print([1,2,3] + [4,5,6])
    # # print([1,2,3] + (4,5,6))
    # a = [1]
    # b = [2]
    # c = (a,b)
    # print(c)
    # b = [3]
    # print(c)
    #
    # d = [1,2,3,4]
    # for i, el in enumerate(d):
    #     d.pop(i)
    # print(d)

    reader = ReaderFactory().create('txt')
    writer = WriterFactory().create('txt')
    with reader('input.txt') as rr, writer('output.bin') as ww:
            ww.write(rr.read_all())
