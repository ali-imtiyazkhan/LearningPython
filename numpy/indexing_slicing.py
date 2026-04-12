import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("1D Array:", arr_1d)

# Basic indexing
print("Element at index 0:", arr_1d[0])
print("Element at index 3:", arr_1d[3])

# Slicing
print("Slicing from index 1 to 4:", arr_1d[1:4])
print("Everything before index 3:", arr_1d[:3])
print("Everything after index 2:", arr_1d[2:])

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:\n", arr_2d)

# 2D indexing [row, column]
print("Element at (1, 1):", arr_2d[1, 1])

# 2D Slicing
print("First two rows:\n", arr_2d[:2, :])
print("Second column of all rows:", arr_2d[:, 1])

# Boolean Indexing
mask = arr_1d > 3
print("\nElements in arr_1d > 3:", arr_1d[mask])
