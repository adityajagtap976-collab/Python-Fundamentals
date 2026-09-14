# Recursive function
def show(n: int) -> None:
    if n == 0:
        return
    print(n)
    show(n - 1)


show(8)
