import numpy as np
# Array Properties
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(arr.shape) #dimensions - (m x n)
print(arr.size) #total elements - m*n
print(arr.ndim) #dimension
print(arr.dtype) #data type object

str_arr = np.array([1, 2, 3], dtype="U")
print(str_arr, str_arr.dtype)

float_arr = np.array([1, 2, 3], dtype="float64")
print(str_arr, float_arr.dtype)

int_arr = float_arr.astype(np.int64)
print(int_arr, int_arr.dtype)