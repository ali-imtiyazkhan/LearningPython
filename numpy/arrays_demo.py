# NumPy: 1D, 2D, and 3D Arrays
"""
In NumPy, dimensions are called 'axes'. 
- A 1D array is like a single list (vector).
- A 2D array is like a table with rows and columns (matrix).
- A 3D array is like a stack of 2D arrays (cube or tensor).
"""

try:
    import numpy as np

    # 1D Array
    # A single list of values
    arr_1d = np.array([10, 20, 30, 40])
    print("--- 1D Array (Vector) ---")
    print(arr_1d)
    print(f"Shape: {arr_1d.shape}") # (4,)
    print("-" * 25)

    # 2D Array
    # A table with rows and columns
    arr_2d = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print("\n--- 2D Array (Matrix) ---")
    print(arr_2d)
    print(f"Shape: {arr_2d.shape}") # (2, 3)
    print("-" * 25)

    # 3D Array
    # A collection of 2D arrays
    arr_3d = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ])
    print("\n--- 3D Array (3D Tensor) ---")
    print(arr_3d)
    print(f"Shape: {arr_3d.shape}") # (2, 2, 2)
    print("-" * 25)

# adding datatype in a numpy array
    arr_type = np.array([1,2,3,4,5],dtype=float)
    print(arr_type)
    print(arr_type.dtype)

except ImportError:
    print("NumPy is not installed. Run 'pip install numpy' to see this code in action!")
