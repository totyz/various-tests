# What will be the output?
if __name__ == '__main__':
    d = [1, 2, 3, 4]
    for i, el in enumerate(d):
        d.pop(i)
    print(d)
