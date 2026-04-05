# Using the zip() function in Python

# 1. Zipping Two Lists
# Combine names with their corresponding scores
names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]

print("--- 1. Basic Zipping ---")
zipped = zip(names, scores)
print(f"Zipped Object: {zipped}") # Returns a zip object (iterator)
print(f"Zipped List: {list(zipped)}")

# 2. Iterating through Multiple Lists Simultaneously
print("\n--- 2. Iterating with zip() ---")
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# 3. Zipping More Than Two Lists
print("\n--- 3. Zipping Multiple Lists ---")
ages = [20, 22, 21, 23]
combined = list(zip(names, scores, ages))
print(f"Combined (Name, Score, Age): {combined}")

# 4. Zipping Lists of Different Lengths
# zip() stops at the shortest list
extra_names = ["Eve", "Frank"]
print("\n--- 4. Zipping Different Lengths ---")
short_zipped = list(zip(extra_names, scores))
print(f"Zipping shorter list with longer list: {short_zipped}")

# 5. Unzipping (The * Operator)
print("\n--- 5. Unzipping ---")
pairs = [('A', 1), ('B', 2), ('C', 3)]
unzipped_chars, unzipped_nums = zip(*pairs)
print(f"Unzipped Chars: {unzipped_chars}")
print(f"Unzipped Nums: {unzipped_nums}")

# 6. Creating a Dictionary with zip()
print("\n--- 6. Creating a Dictionary ---")
score_dict = dict(zip(names, scores))
print(f"Scores Dictionary: {score_dict}")
