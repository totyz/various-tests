# create function get_max(data: str) -> int
# which takes the largest digit from string "4214210949214918248184128" and returns as Int.
# What happens when string contains none digit character? How to modify function to get rid of such characters?

def get_max(data: str) -> int:
    pass

if __name__ == '__main__':
    print(get_max('12'))
    print(get_max('4214210949214918248184128'))
    print(get_max('12ADAM'))