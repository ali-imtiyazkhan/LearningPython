# Different Ways to Traverse (Iterate) through a List

# Sample List
fruits = ["apple", "mango", "banana", "kiwi"]

# 1. Direct Iteration (Iterate by Value)
# This is the most common and readable way when you only need the items.
print("--- 1. Direct Iteration (Value) ---")
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 2. Iterate by Index (Using range and len)
# Useful when you need to know the position or modify the list in place.
print("\n--- 2. Iteration by Index ---")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# 3. Both at Once (Using enumerate)
# This is the recommended way to get both the index AND the value together.
print("\n--- 3. Using enumerate() (Best Practice) ---")
for index, fruit in enumerate(fruits):
    print(f"Index {index} -> {fruit}")

# 4. Reverse Traversal
print("\n--- 4. Reverse Traversal ---")
for fruit in reversed(fruits):
    print(f"Reversed: {fruit}")
