import numpy as np
arr = []
a = int(input("Enter the size of array: "))
print("\nEnter the elements in decimal values: ")
for i in range(a):
    arr.append(float(input("Enter %dth element: " %i)))

arr = np.array(arr)
print("\nOriginal array: ")
print(arr)

new_arr = arr.astype("i")
print("\nConversion of array datatype: ")
print(new_arr)
print("\nDataype of current output: ")
print(new_arr.dtype)