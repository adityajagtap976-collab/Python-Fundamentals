import os

# File Input/Output: Creating a file
with open("C:\\Users\\adity\\practice.txt", "x") as f:
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
with open("C:\\Users\\adity\\practice.txt", "r+") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)

# Searching for a specific word in the file
with open("C:\\Users\\adity\\practice.txt", "r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Found!")
    else:
        print("Not Found")

os.remove("C:\\Users\\adity\\practice.txt")
