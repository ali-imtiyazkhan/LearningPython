# Dictionaries in Python

# 1. Creation and Syntax
# Dictionaries are UNORDERED and MUTABLE collections of KEY:VALUE pairs.
my_dict = {"name": "Alice", "age": 25, "city": "London"}
print(f"--- 1. Creation ---")
print(f"Dictionary: {my_dict}")
print(f"Type: {type(my_dict)}")

# 2. Accessing Elements
# Dictionaries use keys, not indices.
print(f"\n--- 2. Accessing ---")
print(f"Name and Age: {my_dict['name']}, {my_dict['age']}")

# Use get() for a safer retrieval (does not raise KeyError if not found)
print(f"City (using get()): {my_dict.get('city')}")
print(f"Hobby (using get()): {my_dict.get('hobby', 'Not Found!')}")

# 3. Adding and Modifying Elements
# Dictionaries are mutable.
print(f"\n--- 3. Adding and Modifying ---")
my_dict["hobby"] = "Photography"
my_dict["age"] = 30
print(f"Modified Dictionary: {my_dict}")

# 4. Removing Elements
print(f"\n--- 4. Removing ---")
removed_city = my_dict.pop("city")
print(f"Removed city: {removed_city}")
print(f"After .pop('city'): {my_dict}")

del my_dict["age"]
print(f"After 'del my_dict[\"age\"]': {my_dict}")

# 5. Iteration
print(f"\n--- 5. Iterating ---")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

print(f"All Keys: {list(my_dict.keys())}")
print(f"All Values: {list(my_dict.values())}")
