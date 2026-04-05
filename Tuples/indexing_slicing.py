# Indexing and Slicing in Tuples

# 1. Basic Indexing
# Like lists, tuples are 0-indexed.
colors = ("red", "green", "blue", "yellow", "black")
print(f"--- 1. Basic Indexing ---")
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"Second to last color: {colors[-2]}")

# 2. Slicing
# [start:stop:step]
print(f"\n--- 2. Slicing [start:stop:step] ---")
print(f"First three: {colors[:3]}")
print(f"Last two: {colors[-2:]}")
print(f"Middle two (index 1 to 3): {colors[1:3]}")
print(f"Every second color: {colors[::2]}")
print(f"Reversed tuple: {colors[::-1]}")

# 3. Nested Indexing
# Accessing elements inside a tuple within a tuple
nested = (1, 2, ("a", "b", "c"), 3)
print(f"\n--- 3. Nested Indexing ---")
print(f"Nested Tuple: {nested[2]}")
print(f"Char 'b' from nested: {nested[2][1]}")

# 4. Finding Index
print(f"\n--- 4. Finding Index ---")
print(f"Index of 'blue': {colors.index('blue')}")

# Remember: You can index and slice, but you CANNOT change!
# colors[0] = "white"  <-- This will still raise a TypeError
