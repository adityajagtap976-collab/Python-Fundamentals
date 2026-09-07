# --- *args ---
def add_all(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


print(add_all(1, 2, 2))
print(add_all(5, 10, 15, 20))


# --- **kwargs ---
def print_user_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print_user_profile(username="Aditya", role="Admin")
print_user_profile(Name="Omkar", Age=18, city="Mansarover")

# --- scope ---
x = 10  # Global Variable


def show_numbers():
    y = 5  # Local Variable
    print(x)
    print(y)


show_numbers()
print(x)
print(y)


def update_():
    global x
    x = 20


update_()
print(x)

# ---try/except---
try:
    number = int(3)
    print("That's an integer!")
except ValueError:
    print("Oops! That wasn't a valid number. ")
finally:
    print("Execution Finished! ")
