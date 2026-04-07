# NumPy Introduction
"""
NumPy (Numerical Python) is a powerful Python library used for numerical and scientific computing.
It provides support for large, multidimensional arrays and matrices, along with a collection of
high-level mathematical functions to operate on these arrays.

Why Use NumPy?
1. Speed: NumPy arrays are much faster than traditional Python lists for mathematical operations.
2. Memory: They use less memory than Python lists.
3. Functionality: NumPy provides various functions for linear algebra, Fourier transforms, and statistics.

To install NumPy, run this command in your terminal:
    pip install numpy
"""

# Import the library
# Note: Since NumPy isn't installed on this system yet, 
# you'll see an error when you try to run this script until you install it.

try:
    '''

    first we import the numpy and then we insert the array element into it 
    
    '''
    import numpy as np
    array = np.array([1,2,3,4,5])

    print(f"NumPy Array: {array}")
    print(f"Array Shape: {array.shape}")
except ImportError:

    print("NumPy is not installed. Run 'pip install numpy' to get started!")
    
