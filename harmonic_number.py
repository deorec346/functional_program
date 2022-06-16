def harmonic(num):
    """
        Description:
            Function to calculate harmonic value
        Parameter:
            Take input as user entered number to find harmonic value
        Return:
            Calculated harmonic value of input
    """
    value = 0.0
    for i in range(1, num + 1):
        value = value + 1 / i
    return value


if __name__ == '__main__':
    number = int(input("Enter the nth number :"))
    result = harmonic(number)
    print("Value of {}th harmonic number :{}".format(number, result))