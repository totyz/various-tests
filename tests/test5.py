# Create exception_type(ex: Exception) -> str function
# which returns type of exception in string form

def exception_type(ex: Exception) -> str:
    pass

if __name__ == '__main__':
    try:
        sum()
    except Exception as ex:
        print(ex)
        print(exception_type(ex))  # here we should see TypeError
