# Working with Nested Dictionaries in Python

# 1. Creation and Syntax
# Nested dictionaries are dictionaries inside dictionaries.
users = {
    "user1": {"name": "Alice", "age": 25, "role": "Admin"},
    "user2": {"name": "Bob", "age": 30, "role": "Guest"},
    "user3": {"name": "Charlie", "age": 35, "role": "Editor"}
}
print(f"--- 1. Creation ---")
print(f"Users Dictionary: {users}")

# 2. Accessing Elements
# Accessing nested elements by chaining keys.
print(f"\n--- 2. Accessing ---")
print(f"User 1 Name: {users['user1']['name']}")
print(f"User 2 Role: {users['user2']['role']}")

# 3. Modifying Elements
print(f"\n--- 3. Modifying ---")
users['user2']['role'] = "Admin"
print(f"User 2 Updated Role: {users['user2']['role']}")

# 4. Adding Elements
print(f"\n--- 4. Adding ---")
users['user4'] = {"name": "David", "age": 40, "role": "Guest"}
print(f"User 4 Added: {users['user4']}")

# 5. Iterating through Nested Dictionaries
print(f"\n--- 5. Iterating ---")
for user_id, info in users.items():
    print(f"User ID: {user_id}")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")
