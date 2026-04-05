# Comparison between Lists and Strings in Python

# 1. Similarity: Both are sequences (Indexing and Slicing)
name_str = "Python"
name_list = ['P', 'y', 't', 'h', 'o', 'n']

print("--- Similarity: Indexing & Slicing ---")
print(f"String char at index 0: {name_str[0]}")
print(f"List item at index 0: {name_list[0]}")
print(f"String slice [1:4]: {name_str[1:4]}")
print(f"List slice [1:4]: {name_list[1:4]}")
print(f"Length of string: {len(name_str)}")
print(f"Length of list: {len(name_list)}")

# 2. Difference: Mutability
# Lists are mutable (can be changed in place)
# Strings are immutable (cannot be changed once created)

print("\n--- Difference: Mutability ---")
try:
    name_list[0] = 'J'
    print(f"Modified List: {name_list}")
    
    print("Attempting to modify string: name_str[0] = 'J'...")
    name_str[0] = 'J' # This will raise a TypeError
except TypeError as e:
    print(f"Error modifying string: {e}")

# 3. Memory and Modification
# When you "modify" a string, you are actually creating a new object.
# When you modify a list, it's often the same object.

print("\n--- Difference: Memory/Object ID ---")
s1 = "hello"
print(f"Original String ID: {id(s1)}")
s1 = s1 + " world"
print(f"New String ID: {id(s1)} (Different ID because strings are immutable)")

l1 = [1, 2, 3]
print(f"Original List ID: {id(l1)}")
l1.append(4)
print(f"Modified List ID: {id(l1)} (Same ID because lists are mutable)")

# 4. Deleting Elements (del, pop, remove)
# Lists: support all three
# Strings: immutable, so they support none of these for content modification

print("\n--- Difference: Deleting Elements (del, pop, remove) ---")
test_list = ["apple", "banana", "cherry", "date"]
test_str = "apple"

print(f"Original List: {test_list}")
# del: removes by index
del test_list[0]
print(f"List after 'del test_list[0]': {test_list}")

# pop: removes by index and returns it
popped_val = test_list.pop(1)
print(f"List after 'test_list.pop(1)' ({popped_val}): {test_list}")

# remove: removes by value
test_list.remove("date")
print(f"List after 'test_list.remove(\"date\")': {test_list}")

print("\nAttempting 'del test_str[0]'...")
try:
    del test_str[0]
except TypeError as e:
    print(f"Error with 'del' on string: {e}")

print("Attempting 'test_str.pop()'...")
try:
    test_str.pop()
except AttributeError as e:
    print(f"Error: Strings do not have .pop() -> {e}")

print("Attempting 'test_str.remove('a')'...")
try:
    test_str.remove('a')
except AttributeError as e:
    print(f"Error: Strings do not have .remove() -> {e}")

# clear: empties the list
test_list.clear()
print(f"List after 'test_list.clear()': {test_list}")

print("Attempting 'test_str.clear()'...")
try:
    test_str.clear()
except AttributeError as e:
    print(f"Error: Strings do not have .clear() -> {e}")

# 5. Conversion
print("\n--- Conversion ---")
converted_list = list("Apple")
print(f"String to List: {converted_list}")

joined_str = "-".join(['a', 'b', 'c'])
print(f"List to String using join(): {joined_str}")


