import numpy as np
arr = np.array([i for i in range(12)])
print("\nOriginal array: ")
print(arr)
new_arr = arr.reshape(2,3,2)
print("\nArray re-dimensioning: ")
print(new_arr)