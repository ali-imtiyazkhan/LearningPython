# --- Array vs. List: Key Differences ---

# 1. Size (Static vs. Dynamic)
# - Array: In many languages, arrays are of fixed size once created. 
# - List: Python lists are dynamic; they can grow and shrink in size easily 
#   using methods like append() and pop().

# 2. Data Types (Homogeneous vs. Heterogeneous)
# - Array: Stores elements of the SAME data type (Homogeneous). 
# - List: Can store elements of DIFFERENT data types (Heterogeneous), 
#   such as [1, "hello", 3.14].

# 3. Performance (Execution Speed)
# - Array: Faster for numerical calculations because elements are stored 
#   directly in contiguous blocks of memory. 
# - List: Slower because of "Referential Overhead"—it has to follow 
#   memory addresses (pointers) to find every single value.

# 4. Memory Efficiency
# - Array: Very memory efficient because it only stores the raw data.
# - List: Consumes much more memory because it must store the value, 
#   the memory address (pointer), and extra object metadata.

# 5. Convenience & Methods
# - Array: Generally used for mathematical operations; often requires 
#   external libraries like NumPy for advanced features.
# - List: Highly convenient; comes with many built-in methods (sort, 
#   extend, insert, reverse) making it very flexible for general programming.