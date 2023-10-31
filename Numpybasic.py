# bash
pip install numpy
Now, let's go through some basic NumPy operations:

# Import NumPy
import numpy as np

# Creating NumPy Arrays
1. Create a 1D array:
arr = np.array([1, 2, 3, 4, 5])
print(arr)
2. Create a 2D array (matrix):
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
3. Create arrays filled with zeros or ones:
zeros = np.zeros(5)  # Creates a 1D array of zeros with 5 elements
ones = np.ones((3, 3))  # Creates a 3x3 matrix of ones

# Array Attributes
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)      # Shape of the array
print(arr.ndim)       # Number of dimensions
print(arr.size)       # Number of elements in the array
print(arr.dtype)      # Data type of the elements

# Basic Array Operations
Element-wise operations:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

# Array Broadcasting:
a = np.array([1, 2, 3])
b = 2  # Scalar

result = a + b  # Broadcasting the scalar to each element of 'a'

#Indexing and Slicing
arr = np.array([1, 2, 3, 4, 5])

print(arr[0])       # Access a single element
print(arr[1:4])     # Slicing
print(arr[::2])     # Slicing with a step

# Reshaping Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)  # Reshape to a 2x3 matrix
Random Number Generation
random_numbers = np.random.rand(3, 3)  # Generate a 3x3 array of random numbers between 0 and 1

# Array Functions
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

mean = np.mean(arr)     # Mean
median = np.median(arr) # Median
std_dev = np.std(arr)   # Standard deviation
