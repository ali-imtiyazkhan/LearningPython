# Loops in Python (Iterating over Lists and Strings)

# 1. 'for' Loop Over a List
print("--- Iterating over a List ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# 2. 'for' Loop Over a String
print("\n--- Iterating over a String ---")
word = "Python"
for char in word:
    print(f"Character: {char}")

# 3. Using range() to iterate by index
print("\n--- Using range() with index ---")
for i in range(len(fruits)):
    print(f"Fruit at index {i} is {fruits[i]}")

# 4. Using enumerate() - Get both index and value
print("\n--- Using enumerate() ---")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 5. 'while' Loop with List
print("\n--- 'while' Loop over a List ---")
index = 0
while index < len(fruits):
    print(f"While loop: {fruits[index]}")
    index += 1

# 6. Nested Loops (Looping through a list of lists)
print("\n--- Nested Loops ---")
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for num in row:
        print(f"Element: {num}")

# 7. List Comprehension (Short-hand for loops)
print("\n--- List Comprehension (Bonus) ---")
squared = [x**2 for x in range(1, 6)]
print(f"Squares: {squared}")
