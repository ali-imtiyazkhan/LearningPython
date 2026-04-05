# Sets in Python

# 1. Creation and Syntax
# Sets are UNORDERED and UNINDEXED collections of UNIQUE elements.
my_set = {1, 2, 3, 4, 1, 2} # Duplicates are removed automatically
print(f"--- 1. Creation ---")
print(f"Set (Duplicates Removed): {my_set}")
print(f"Type: {type(my_set)}")

# 2. Accessing Elements
# Sets are unindexed, so you cannot use [index]. Instead, use iteration or check existence.
print(f"\n--- 2. Accessing ---")
for x in my_set:
    print(f"Set item: {x}")

print(f"Is 3 inside? {3 in my_set}")

# 3. Adding and Removing Elements
# Sets are MUTABLE (can be changed).
print(f"\n--- 3. Adding and Removing ---")
my_set.add(10)
print(f"Set after .add(10): {my_set}")

my_set.remove(1) # Raises KeyError if not found
my_set.discard(100) # Does NOT raise error if not found
print(f"Set after .remove(1): {my_set}")

# 4. Set Mathematical Operations
# Set union, intersection, and difference are very powerful.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(f"\n--- 4. Set Math ---")
print(f"Union (s1 | s2): {s1 | s2}") # Combined
print(f"Intersection (s1 & s2): {s1 & s2}") # Overlap
print(f"Difference (s1 - s2): {s1 - s2}") # Unique to s1
print(f"Symmetric Difference (s1 ^ s2): {s1 ^ s2}") # Unique to both
