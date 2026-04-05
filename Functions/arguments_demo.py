# Types of Function Arguments in Python

# 1. Positional Arguments
# The most common type. Arguments are passed based on their order.
def greet(name, msg):
    print(f"Hello {name}, {msg}")

print("--- 1. Positional Arguments ---")
greet("Alice", "Good morning!") # name=Alice, msg=Good morning!

# 2. Default Arguments
# You can provide a default value if the argument is not passed.
def greet_default(name, msg="Good morning!"):
    print(f"Hello {name}, {msg}")

print("\n--- 2. Default Arguments ---")
greet_default("Bob") # Uses default msg
greet_default("Charlie", "How are you?") # Overwrites default msg

# 3. Keyword (Named) Arguments
# Arguments are passed using the parameter names, so order doesn't matter.
print("\n--- 3. Keyword Arguments ---")
greet(msg="What's up?", name="David") # Order is swapped, but it works!

# 4. Variable-length Arguments (*args and **kwargs)
# *args: Collects extra positional arguments into a tuple.
def sum_all(*numbers):
    total = sum(numbers)
    print(f"Sum of {numbers}: {total}")

print("\n--- 4. Variable-length (*args) ---")
sum_all(1, 2, 3, 4, 5)

# **kwargs: Collects extra keyword arguments into a dictionary.
def print_user_info(**info):
    print("User Info:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\n--- 5. Variable-length (**kwargs) ---")
print_user_info(name="Eve", age=28, city="Berlin")
