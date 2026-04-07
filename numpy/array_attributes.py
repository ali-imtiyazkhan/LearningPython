# NumPy: Array Attributes (ndim, shape, size, dtype, itemsize)
"""
This file demonstrates the most important attributes of a NumPy array.
"""

try:
    import numpy as np

    # Create a 2D array for demonstration
    arr = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ], dtype=np.int32)

    print("--- NumPy Array Attributes ---")
    print(f"Array:\n{arr}")
    print("-" * 25)

    # 1. ndim: Number of dimensions
    print(f"1. .ndim (Number of axes): {arr.ndim}")

    # 2. shape: Size of each dimension (rows, columns)
    print(f"2. .shape (Dimensions): {arr.shape}")

    # 3. size: Total number of elements
    print(f"3. .size (Total elements): {arr.size}")

    # 4. dtype: Data type of the elements
    print(f"4. .dtype (Data type): {arr.dtype}")

    # 5. itemsize: Size of each element in bytes
    print(f"5. .itemsize (Bytes per element): {arr.itemsize}")

    # 6. nbytes: Total bytes consumed by the elements of the array
    print(f"6. .nbytes (Total size in bytes): {arr.nbytes}")
    print("-" * 25)

    # Demonstrate changes with a 3D array
    arr_3d = np.zeros((2, 2, 2))
    print("\n--- 3D Array Comparison ---")
    print(f"Shape: {arr_3d.shape}")
    print(f"Dimensions (ndim): {arr_3d.ndim}")
    print(f"Total size: {arr_3d.size}")
    print("-" * 25)

except ImportError:
    print("NumPy is not installed. Run 'pip install numpy' to see this code in action!")
