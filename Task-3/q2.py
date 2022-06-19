import numpy as np
a = np.random.randint(0,2,6)
print("Enter the 1st array: ")
print(a)
b = np.random.randint(0,2,6)
print("Enter the 2nd array: ")
print(b)
print("Result of arrays whether equal or not: ")
arr_eq = np.allclose(a,b)
print(arr_eq)

