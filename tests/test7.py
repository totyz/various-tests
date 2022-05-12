# Create function hex_dec_str(data: str) -> str which takes data string and returns it in 2-digit form
# e.g.
# data: '131415ff43ed' -> '12 14 15 ff 43 ed'
# data: '13' -> '13'
# data: '1' -> '1'
# data: '131' -> '12 1'

def hex_dec_str(data: str) -> str:
    pass

if __name__ == '__main__':
    print(hex_dec_str('1'))
    print(hex_dec_str('13'))
    print(hex_dec_str('131'))
    print(hex_dec_str('131415ff43ed'))
