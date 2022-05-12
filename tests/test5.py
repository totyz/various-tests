# Create exception_type(ex: Exception) -> str function
# which returns type of exception in string form

def exception_type(ex: Exception) -> str:
    return type(ex).__name__

if __name__ == '__main__':
    try:
        sum()
    except Exception as ex:
        print(ex)
        print(exception_type(ex))
