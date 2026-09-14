# Function to get the length of an already defined list.
def length(items: list[int]) -> int:
    items = [1, 2, 5, 6, 4, 8, 9, 5, 4, 2]
    return len(items)


print(length([]))

# Function to get the length of a user defined list,


def get_length(items: list[str]) -> int:
    return len(items)


user_input = input("Enter values for the list.").split()

print(get_length(user_input))


# Function to print the elements of a list in a single line.
def print_elements(items: list[str]) -> list[str]:
    print(items)
    return items


user_input = input("Enter the elements to print. ").split()

print_elements(user_input)


# Write a recursive function to print all elements in a list.
def print_list(items: list[str], index: int = 0) -> None:
    if index == len(items):
        return
    print(items[index])
    print_list(items, index + 1)


fruits = ["Mango", "Apple", "Banana", "Cherry", "Orange"]
print_list(fruits)
