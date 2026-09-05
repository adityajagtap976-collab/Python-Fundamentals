# --- List ---
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Date")  # Inserts the value "Date" at the end of the list.
fruits[0] = "Avocado"  # Updates the value at index 0: "Apple" -> "Avocado".
print(fruits)

# --- Tuple ---
point = (3, 4)
print(point[1])  # Fetches the value at index 1 (4).

# --- Dict ---
student = {"Name": "Aditya", "Age": 19}
student["Age"] = 18  # Updates the value on the key (Age).
student["Major"] = "BCA"  # Adds a new key value pair.
print(student)
print(student["Name"])  # Fetches the value of the pair (Name).

# --- Set ---
numbers = [1, 2, 2, 3, 3, 3]
unique = set(
    numbers
)  # Converts the list into a set, automatically dropping duplicates. Output: {1, 2, 3}.
print(unique)

# --- List Comprehension ---
squares = [x * x for x in range(5)]
print(squares)

fruits = ["Apple", "Banana", "Cherry"]
unique = {1, 2, 3}

# --- Dict Comprehension ---
word_lengths = {word: len(word) for word in fruits}
print(word_lengths)

# --- Checking Membership ---
print("Apple" in fruits)
print("Banana" in unique)

fruits = {"Apple", "Banana", "Cherry"}
word_lengths = {}
for word in fruits:
    word_lengths[word] = len(word)

print(word_lengths)
