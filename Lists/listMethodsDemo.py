# Demonstrating List Methods: append(), extend(), and insert()

# Initial list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# 1. append(item) - Adds a single item to the end of the list
print("\n--- Testing append() ---")
fruits.append("orange")
print("After append('orange'):", fruits)

# 2. extend(iterable) - Adds all items from another list (or any iterable) to the end
print("\n--- Testing extend() ---")
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print("After extend(['mango', 'grape']):", fruits)

# 3. insert(index, item) - Adds an item at a specific position
# Note: index 1 is the second position
print("\n--- Testing insert() ---")
fruits.insert(1, "blueberry")
print("After insert(1, 'blueberry'):", fruits)

# Summary of differences
print("\n--- Summary of results ---")
print(f"Final fruit list: {fruits}")
print(f"Total number of fruits: {len(fruits)}")
