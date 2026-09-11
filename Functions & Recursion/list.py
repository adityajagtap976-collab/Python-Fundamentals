# Function to get the length of an already defined list.
def length(list):
    list = [1, 2, 5, 6, 4, 8, 9, 5, 4, 2]
    return len(list)


print(length(list))

# Function to get the length of a user defined list,


def get_length(list):
    return len(list)


user_input = input("Enter values for the list.").split()

print(get_length(user_input))


# Function to print the elements of a list in a single line.
def print_elements(list):
    print(list)
    return list


user_input = input("Enter the elements to print. ").split()

print_elements(user_input)
