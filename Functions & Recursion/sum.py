# Function Defination
def calcSum(a, b):  # Parameters
    return a + b


print(calcSum(6, 8))  # Function call; arguments


# Average of 3 numbers
def average(a, b, c):
    return a + b + c // 3


print(average(6, 4, 98))


# Multiplication with default parameters
def cal_prod(a=5, b=7):
    return a * b


print(cal_prod())
