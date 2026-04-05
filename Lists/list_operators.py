# Operators on Lists in Python

# 1. Concatenation (+) - Joins two lists together
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("--- Concatenation (+) ---")
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Combined List: {combined}")

# 2. Repetition (*) - Repeats a list a specified number of times
repeated = list1 * 3
print("\n--- Repetition (*) ---")
print(f"List 1 repeated 3 times: {repeated}")

# 3. Membership (in, not in) - Checks if an item is present
print("\n--- Membership (in, not in) ---")
print(f"Is 2 in List 1? {2 in list1}")
print(f"Is 5 in List 1? {5 in list1}")
print(f"Is 10 not in List 1? {10 not in list1}")

# 4. Comparison (==, !=, <, >, <=, >=)
# Lists are compared element by element, from left to right.
l_a = [1, 2, 3]
l_b = [1, 2, 3]
l_c = [1, 2, 4]
l_d = [1, 2]

print("\n--- Comparison ---")
print(f"[1, 2, 3] == [1, 2, 3]: {l_a == l_b}")
print(f"[1, 2, 3] == [1, 2, 4]: {l_a == l_c}")
print(f"[1, 2, 3] < [1, 2, 4]: {l_a < l_c} (3 < 4)")
print(f"[1, 2, 3] > [1, 2]: {l_a > l_d} (More elements or bigger elements first)")

# Common use case: List in for loop
print("\n--- Using 'in' for-loop iteration ---")
for num in list1:
    print(f"Processing number: {num}")
