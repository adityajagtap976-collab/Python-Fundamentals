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
