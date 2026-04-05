import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]

print("--- 1. Assignment (=) ---")
# Both variables point to the same object
assigned = original
print(f"Original ID: {id(original)}")
print(f"Assigned ID: {id(assigned)} (Same as Original)")

assigned[0][0] = 'X'
print(f"After modifying assigned[0][0]:")
print(f"Original: {original}")
print(f"Assigned: {assigned}")

print("\n--- 2. Shallow Copy (copy.copy() or list.copy()) ---")
# Creates a new outer list, but keeps references to nested objects
original = [[1, 2, 3], [4, 5, 6]] # Reset
shallow = original.copy()

print(f"Original ID: {id(original)}")
print(f"Shallow ID:  {id(shallow)} (Different ID)")
print(f"Nested ID (Index 0): {id(original[0])} vs {id(shallow[0])} (Same ID!)")

shallow[0][0] = 'Y'
print(f"After modifying shallow[0][0]:")
print(f"Original: {original} (Modified because nested ID is shared)")
print(f"Shallow:  {shallow}")

print("\n--- 3. Deep Copy (copy.deepcopy()) ---")
# Creates a new outer list AND new nested objects recursively
original = [[1, 2, 3], [4, 5, 6]] # Reset
deep = copy.deepcopy(original)

print(f"Original ID: {id(original)}")
print(f"Deep ID:     {id(deep)} (Different ID)")
print(f"Nested ID (Index 0): {id(original[0])} vs {id(deep[0])} (Different ID!)")

deep[0][0] = 'Z'
print(f"After modifying deep[0][0]:")
print(f"Original: {original} (Unchanged!)")
print(f"Deep:     {deep}")
