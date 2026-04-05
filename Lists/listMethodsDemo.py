# Demonstrating List Methods: append(), extend(), and insert()

# Initial list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# output : ['apple', 'banana', 'cherry']

print("\n")
# 1. append(item) - Adds a single item to the end of the list
print("--- Testing append() ---")
fruits.append("orange")
print("After append('orange'):", fruits)

# output : ['apple', 'banana', 'cherry', 'orange']

# 2. extend(iterable) - Adds all items from another list (or any iterable) to the end
print("\n")
print("\n--- Testing extend() ---")
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print("After extend(['mango', 'grape']):", fruits)

# output : ['apple', 'banana', 'cherry', 'orange', 'mango', 'grape']

# 3. insert(index, item) - Adds an item at a specific position
# Note: index 1 is the second position

print("\n")
print("\n--- Testing insert() ---")
fruits.insert(1, "blueberry")
print("After insert(1, 'blueberry'):", fruits)

# output : ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'mango', 'grape']


print("\n")
# Summary of differences
print("\n--- Summary of results ---")
print(f"Final fruit list: {fruits}")
print(f"Total number of fruits: {len(fruits)}")

print("\n")
print("\n--- Testing extend() with a single item ---")
fruits.extend(["apple"])
print("After extend(['apple']):", fruits)

# output : ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'mango', 'grape', 'apple']

print("\n")
print("\n--- Testing append() with a list ---")
fruits.append(["apple"])
print("After append(['apple']):", fruits)

# output : ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'mango', 'grape', 'apple', ['apple']]


print("\n")
print("\n--- Testing extend() with a string ---")
fruits.extend("apple")
print(fruits)


# output : ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'mango', 'grape', 'apple', ['apple'], 'a', 'p', 'p', 'l', 'e']

