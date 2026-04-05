# List Comprehension in Python

# 1. Basic List Comprehension
# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(f"Traditional Squares: {squares}")

# Using List Comprehension
squares_lc = [i**2 for i in range(1, 6)]
print(f"List Comprehension Squares: {squares_lc}")

# 2. Filtering with 'if'
# Get even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"\nEven Numbers: {evens}")

# 3. Transformation with 'if-else'
# Label numbers as Even or Odd
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(f"\nLabels (Even/Odd): {labels}")

# 4. Nested List Comprehension
# Flattening a 2D matrix
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print(f"\nFlattened Matrix: {flattened}")

# Transposing a matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Transposed Matrix: {transposed}")

# 5. Extracting from Strings
# Convert string to list of characters upper()
word = "python"
chars = [char.upper() for char in word]
print(f"\nUPPERCASE characters: {chars}")


print("\n")

L11 = [1,2,3]
n = -2

print(L11*n)

print("\n")

L12 = [1,2,3]
n = 2

print(L12*n)