# Function to find the factorial of n. (n is the parameter)
def factorial(n: int) -> int | str:
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(5))


# Recursion function to find the factorial
def factorial_r(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial_r(n - 1)


print(factorial_r(4))
