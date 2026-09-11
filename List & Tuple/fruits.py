# --- List ---
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Date")  # Inserts the value "Date" at the end of the list.
fruits[0] = "Avocado"  # Updates the value at index 0: "Apple" -> "Avocado".
print(fruits)

# --- Tuple ---
point = (3, 4)
print(point[1])  # Fetches the value at index 1 (4).

# --- List Comprehension ---
squares = [x * x for x in range(5)]
print(squares)

fruits = ["Apple", "Banana", "Cherry"]
unique = {1, 2, 3}
