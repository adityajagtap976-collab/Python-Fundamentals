import os

FILE_PATH = r"C:\Users\adity\practice.txt"
# File Input/Output: Creating a file
with open(FILE_PATH, "x") as f:
    f.write(
        "Hi everyone"
        + "\n"
        + "we are learning File I/O"
        + "\n"
        + "using Java."
        + "\n"
        + "I like programming in Java."
    )

# Reading and replacing content in the file
with open(FILE_PATH, "r+") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)

# Searching for a specific word in the file
with open(FILE_PATH, "r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Found!")
    else:
        print("Not Found")

# Finding the line number of a specific word in the file
with open(FILE_PATH, "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        if "learning" in line:
            print(line_no)

# From a file containing numbers by comma, print the count of even numbers.
with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write("1,2,3,4,5,6,7,8,9,10")
with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = f.read()
    numbers = [int(x) for x in data.split(",")]
    even_count = sum(1 for x in numbers if x % 2 == 0)
    print(even_count)

os.remove(FILE_PATH)
