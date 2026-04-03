# --- How Python Lists are Stored in Memory ---

# 1. Referential Array
# Instead of storing values directly inside the array, Python lists store the 
# memory ADDRESS (reference) of each value. 
# This is called a "Referential Array."

# 2. Why use addresses? (Benefits)
# - Heterogeneity: A single list can store different data types (int, str, list) 
#   because every memory address is of the same size, even if the values 
#   they point to are of different sizes.
# - Efficient Movement: Moving items (like sorting or swapping) only requires 
#   swapping the small memory addresses, not the large objects themselves.

# 3. How it looks in RAM:
# [List Object] -> [Array of Addresses: 0x11, 0x5a, 0x7c]
#                       |           |           |
#                       v           v           v
#                   [Int: 10]   [Str: 'Hi']  [Float: 3.14]

# 4. Access Speed
# - Accessing an element is O(1) because fixed-size addresses allow the CPU 
#   to jump directly to any index.
# - However, it is slightly slower than a "Dense Array" (like in C or NumPy) 
#   because Python must "dereference" the address to find the actual value.

# 5. Dynamic Resizing
# - Python lists are dynamic. When the list is full and you add a new item, 
#   Python allocates a new, larger block of memory (usually doubling it) 
#   and copies the addresses over.




# this will return the address of the value 2  
a = 2
print(id(a))

# this will return the address of the list L and the address of the values in the list L
L = [1,2,3]
print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))

# this is also the same it will also print the address of the values in the list L
print(id(1))
print(id(2))
print(id(3))
