import numpy as np
arr1 = np.array([1,6,3,4,8])
arr2 = np.array([2,5,0,1,3])
arr3 = arr1 + arr2
print("       ",arr3)

# using a loop
arr3 = []
k = 0
for num1 in arr1:
    arr3.append(num1 + arr2[k])
    k+=1
print("sum is ", arr3)
