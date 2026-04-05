# Tuples in Python

# 1. Creation and Syntax
# Tuples are IMMUTABLE (cannot be changed after creation) and ordered.
my_tuple = (10, 20, 30, 40, 50)
print(f"--- 1. Creation ---")
print(f"Tuple: {my_tuple}")
print(f"Type: {type(my_tuple)}")

# 2. Accessing Elements
print(f"\n--- 2. Accessing ---")
print(f"Element at index 0: {my_tuple[0]}")
print(f"Slicing [1:4]: {my_tuple[1:4]}")

# 3. Immutability
print(f"\n--- 3. Immutability ---")
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"Error: {e} (Tuples cannot be modified!)")

# 4. Tuple Packing and Unpacking
print(f"\n--- 4. Packing and Unpacking ---")
packed = "Apple", "Banana", "Cherry" # Packing
a, b, c = packed # Unpacking
print(f"Packed: {packed}")
print(f"Unpacked: a={a}, b={b}, c={c}")

# 5. Common Methods (only two: count and index)
print(f"\n--- 5. Methods ---")
numbers = (1, 2, 3, 2, 4, 2)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 4: {numbers.index(4)}")
