# Common Dictionary Methods in Python

# 1. .update() - Update the dictionary from another dictionary or iterable
person = {"name": "Alice", "age": 25}
person.update({"age": 26, "city": "London"}) # Updates existing key and adds new one
print(f"--- 1. .update() ---")
print(f"Updated person dictionary: {person}")

# 2. .setdefault() - Returns value of key, or inserts it with a default if not found
age = person.setdefault("age", 30) # Key exists, returns existing value
hobby = person.setdefault("hobby", "Unspecified") # Key missing, inserts "Unspecified"
print(f"\n--- 2. .setdefault() ---")
print(f"Age (existing): {age}")
print(f"Hobby (inserted): {hobby}")
print(f"Dictionary after setdefault: {person}")

# 3. .fromkeys() - Create a new dictionary with specified keys and a single value
keys = ["a", "b", "c"]
initial_value = 0
new_dict = dict.fromkeys(keys, initial_value)
print(f"\n--- 3. .fromkeys() ---")
print(f"New dictionary from keys: {new_dict}")

# 4. .clear() - Empties the dictionary completely
print(f"\n--- 4. .clear() ---")
new_dict.clear()
print(f"After .clear(): {new_dict}")

# 5. .copy() - Shallow copy the dictionary
copy_person = person.copy()
print(f"\n--- 5. .copy() ---")
print(f"Original ID: {id(person)}")
print(f"Copy ID: {id(copy_person)} (Different ID, same contents)")
