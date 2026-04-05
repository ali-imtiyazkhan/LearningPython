# Introduction to Tuples in Python

# 1. Definition
# A tuple in Python is similar to a list. 
# The main difference is that a tuple is IMMUTABLE (cannot be changed) 
# and a list is MUTABLE (can be changed).

# 2. Creating Tuples
# Tuples use parentheses () instead of square brackets [].
fruits = ("apple", "banana", "cherry")
empty_tuple = ()
print(f"Fruits Tuple: {fruits}")

# IMPORTANT: To create a tuple with only ONE element, you MUST include a trailing comma.
single_tuple = ("apple",) # Correct
not_a_tuple = ("apple")   # This is just a string!

print(f"Type of single_tuple: {type(single_tuple)}")
print(f"Type of not_a_tuple: {type(not_a_tuple)}")

# 3. Accessing Elements (Ordered)
# Just like lists, tuples are ordered and indexed.
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# 4. Immutability (The Core Feature)
# You cannot add, remove, or change elements after creation.
try:
    fruits[0] = "mango"
except TypeError as e:
    print(f"\nExample of Immutability: {e}")

# 5. When to use Tuples?
# - When you want to ensure data cannot be modified accidentally.
# - When you are returning multiple values from a function.
# - Tuples are slightly faster than lists for constant data.