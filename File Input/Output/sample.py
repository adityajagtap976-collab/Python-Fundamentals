# File Input/Output: Reading
with open("C:\\Users\\adity\\sample.txt", "r") as f:
    data = f.read()
    lines = f.readlines()
    print(data)
    print(lines)

# File Input/Output: Writing
with open("C:\\Users\\adity\\sample.txt", "w+") as f:
    f.write("Hi I am Aditya")
    f.seek(0)
    data = f.read()
    print(data)
    print(f.tell())

# File Input/Output: Appending
with open("C:\\Users\\adity\\sample.txt", "a+") as f:
    f.write(
        "\n"
        + "and I am learning Python"
        + "\n"
        + "I study at Pillai's University"
        + "\n"
        + "and I am in the 2nd year of my B.C.A course"
    )
    f.seek(0)
    data = f.read()
    print(data)


# Character       Meaning
# r               Read
# w               Write
# a               Append
# x               Create
# r+              Read and Write
# w+              Write and Read
# a+              Append and Read

# Pointer and Stream Positioning:
# The seek() method is used to change the position of the file pointer.
# The tell() method is used to get the current position of the file pointer.
