# --- scope ---
x = 10  # Global Variable


def show_numbers():
    y = 5  # Local Variable
    print(x)
    print(y)


show_numbers()
print(x)
# print(y)


def update_():
    global x
    x = 20


update_()
print(x)
