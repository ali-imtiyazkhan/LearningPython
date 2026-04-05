# Functions in Python - Even Number Check

# 1. Defining a Function
# A function is a block of code that only runs when it is called.
def is_even(number):
    """
    Returns True if the number is even, False otherwise.
    """
    if number % 2 == 0:
        return True
    else:
        return False

# 2. Calling the Function
print("--- Checking Numbers ---")
test_numbers = [10, 15, 22, 33, 44]

for num in test_numbers:
    if is_even(num):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# 3. Concise way to write the same function
def check_even_short(n):
    return n % 2 == 0

print(f"\nShort check for 50: {check_even_short(50)}")
