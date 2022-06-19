import numpy as np
a = int(input("Enter the first number: "))
b = int(input("Enter the last number: "))
arr=[]
for i in range(a,b+1):
    arr.append(i)
print("\nOriginal array:")
print(arr)
p = 5
new_arr = np.zeros(len(arr) + (len(arr)-1)*(p))
for j in range(len(arr)):
    new_arr[::p+1] = arr
print("\nNew array:")
print(new_arr)