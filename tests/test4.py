# create function get_max(data: str) -> int
# which takes the largest digit from string "4214210949214918248184128" and returns as Int.
# What happens when string contains none digit character? How to modify function to get rid of such characters?

def get_max(el: str):
    return max(map(lambda x: int(x, 0), [x for x in set(el) if '\x30' <= x <= '\x39']))

def get_max(x):
    print(x)
    return max([i for i in x if i.isdigit()])

if __name__ == '__main__':
    print(get_max('12'))
    print(get_max('4214210949214918248184128'))
    print(get_max('12ADAM'))