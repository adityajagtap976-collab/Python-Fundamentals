# --- if / elif / else ---

age = 27

if age < 13:
    catagory = "child"
elif age < 20:
    catagory = "teenager"
else:
    catagory = "adult"

print(catagory)

# --- for loop ---

numbers = [4, 7, 2, 9, 5]

total = 0
for number in numbers:
    total = total + number

print(total)

# --- for loop with range ---

for i in range(5):
    print(i)

# --- while loop ---
countdown = 5
while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("liftoff")

# --- function definition and call ---


def classify_age(age: int) -> str:
    if age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    else:
        return "adult"


print(classify_age(18))
print(classify_age(8))

# --- function with default argument ---


def greet(name: str, greeting: str = "Hello") -> str:
    return greeting + ", " + name


print(greet("Sam"))
print(greet("Sam", "Yo"))
