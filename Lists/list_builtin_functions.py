# Built-in Functions for Lists in Python

# Sample data
numbers = [40, 10, 30, 50, 20]
mixed_truths = [True, False, True]
all_false = [False, False]

# 1. len() - Get the length of the list
print(f"--- len() ---")
print(f"Length of numbers: {len(numbers)}")

# 2. min() and max() - Get the smallest and largest values
print(f"\n--- min() and max() ---")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")

# 3. sum() - Get the total sum of numeric elements
print(f"\n--- sum() ---")
print(f"Sum of numbers: {sum(numbers)}")

# 4. sorted() vs list.sort()
# sorted(): Returns a NEW sorted list, original remains unchanged
# list.sort(): Sorts the ORIGINAL list in place
print(f"\n--- Sorting ---")
new_sorted = sorted(numbers)
print(f"Original after sorted(): {numbers}")
print(f"New sorted list: {new_sorted}")

numbers.sort()
print(f"Original after numbers.sort(): {numbers}")

# 5. any() and all()
print(f"\n--- any() and all() ---")
print(f"Numbers (any): {any(numbers)} (True if any element is non-zero/True)")
print(f"Mixed (any): {any(mixed_truths)}")
print(f"Mixed (all): {all(mixed_truths)} (True only if ALL elements are True)")
print(f"All False (any): {any(all_false)}")

# 6. reversed() - Returns an iterator that yields elements in reverse
print(f"\n--- reversed() ---")
rev_iterator = reversed(numbers)
print(f"Reversed list: {list(rev_iterator)}")

# 7. zip() - Combine two lists into pairs (Bonus)
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
combined = list(zip(names, scores))
print(f"\n--- zip() ---")
print(f"Names and Scores paired: {combined}")
