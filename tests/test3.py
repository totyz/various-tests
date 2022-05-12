# Create function solution() -> List
# which returns list of all numbers divided by 4 from range <10, 260>

def solution():
    return [x for x in range(10,261) if x % 4 == 0]

if __name__ == '__main__':
    print(solution())