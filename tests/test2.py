# What the code does?
# What will be the output?
# how to fix it?
if __name__ == '__main__':
    d = [3, 11, 5, 22, 4, 33, 5]
    for i, el in enumerate(d):
        if i > 0 and i % 2 == 0:
            d.pop(i)
    print(d)  # wrong, remove from enumerated list which become shorter

    # Filtering by creating new list
    n = []
    for i, el in enumerate(d):
        if i > 0 and i % 2 == 0:
            n.append(el)
    print(n)

    # Filtering by list comp
    print([el for i, el in enumerate(d) if i > 0 and i % 2 == 0])
