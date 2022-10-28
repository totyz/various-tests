# What the code does?
# What will be the output?
# how to fix it?
if __name__ == '__main__':
    d = [3, 11, 5, 22, 4, 33, 5]
    for i, el in enumerate(d):
        if i > 0 and i % 2 == 0:
            d.pop(i)
    print(d)
