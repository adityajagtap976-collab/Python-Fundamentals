# Function Defination
def calcSum(a: int, b: int) -> int:  # Parameters
    return a + b


print(calcSum(6, 8))  # Function call; arguments


# Average of 3 numbers
def average(a: int, b: int, c: int) -> int:
    return a + b + c // 3


print(average(6, 4, 98))


# Multiplication with default parameters
def cal_prod(a: int = 5, b: int = 7) -> int:
    return a * b


print(cal_prod())


# Recursive function to calculate the sum of first n natural numbers.
def sum_of_natural(n: int) -> int:
    if n == 0:
        return 0
    return sum_of_natural(n - 1) + n


print(sum_of_natural(3))
