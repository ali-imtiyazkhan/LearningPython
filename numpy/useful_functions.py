# NumPy: Common Functions (arange, reshape, ones, zeros)
"""
This file demonstrates some of the most useful array creation and manipulation functions in NumPy.
"""

try:
    import numpy as np

    # 1. np.arange(start, stop, step)
    # Creates an array with a range of numbers, similar to Python's range()
    arr_arange = np.arange(0, 10) # 0 to 9
    print("--- np.arange(0, 10) ---")
    print(arr_arange)
    print("-" * 25)

    # 2. np.linspace(start, stop, num)
    # Creates an array with 'num' evenly spaced numbers between 'start' and 'stop' (inclusive)
    arr_linspace = np.linspace(0, 1, 5) # 5 numbers between 0 and 1
    print("\n--- np.linspace(0, 1, 5) ---")
    print(arr_linspace)
    print("-" * 25)

    # 2. np.reshape(rows, cols)
    # Changes the shape of an existing array without changing its data.
    # Note: The total number of elements must remain the same!
    arr_reshaped = arr_arange.reshape(2, 5) # 2 rows, 5 columns (2 * 5 = 10)
    print("\n--- .reshape(2, 5) ---")
    print(arr_reshaped)
    print("-" * 25)

    # 3. np.ones(shape)
    # Creates an array filled with 1.0 (float by default)
    arr_ones = np.ones((3, 3)) # 3x3 square matrix of ones
    print("\n--- np.ones((3, 3)) ---")
    print(arr_ones)
    print("-" * 25)

    # 4. np.zeros(shape)
    # Creates an array filled with 0.0 (float by default)
    arr_zeros = np.zeros((2, 4)) # 2 rows, 4 columns of zeros
    print("\n--- np.zeros((2, 4)) ---")
    print(arr_zeros)
    print("-" * 25)

    # 5. np.random.randint(low, high, size)
    # Creates an array with random integers between low (inclusive) and high (exclusive)
    arr_random = np.random.randint(1, 100, (2, 3)) # 2x3 array of random ints 1-99
    print("\n--- np.random.randint(1, 100, (2, 3)) ---")
    print(arr_random)
    print("-" * 25)

    # 6. Statistical Functions (max, min, sum, mean)
    print("\n--- Statistical Functions on Random Array ---")
    print(f"Random Array:\n{arr_random}")
    print(f"Max: {np.max(arr_random)}")
    print(f"Min: {np.min(arr_random)}")
    print(f"Sum: {np.sum(arr_random)}")
    print(f"Mean: {np.mean(arr_random):.2f}")
    print("-" * 25)



except ImportError:
    print("NumPy is not installed. Run 'pip install numpy' to see this code in action!")