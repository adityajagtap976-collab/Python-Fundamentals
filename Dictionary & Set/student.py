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

# --- Dict Comprehension ---
fruits = {"Apple", "Banana", "Cherry"}
print("Banana" in fruits)

word_lengths = {}
for word in fruits:
    word_lengths[word] = len(word)

print(word_lengths)
