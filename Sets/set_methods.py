# Common Set Methods in Python

# 1. update() - Used to add multiple elements at once (from a list, tuple, or set)
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(f"--- 1. .update() ---")
print(f"Set after .update([4, 5, 6]): {my_set}")

# 2. pop() - Removes and returns a RANDOM element (as sets are unordered)
print(f"\n--- 2. .pop() ---")
popped = my_set.pop()
print(f"Popped element: {popped}")
print(f"After .pop(): {my_set}")

# 3. clear() - Empties the set completely
print(f"\n--- 3. .clear() ---")
my_set.clear()
print(f"After .clear(): {my_set}")

# 4. issubset() and issuperset()
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
print(f"\n--- 4. Subset and Superset ---")
print(f"Is s2 a subset of s1? {s2.issubset(s1)}")
print(f"Is s1 a superset of s2? {s1.issuperset(s2)}")

# 5. isdisjoint() - Returns True if two sets have NO intersection
s3 = {8, 9, 10}
print(f"\n--- 5. isdisjoint() ---")
print(f"Are s1 and s3 disjoint? {s1.isdisjoint(s3)}")
