# ways of creating arrays using numpy

from numpy import *
# using numpy module mentioning of typecode in array is optional
# 1. array()
# arr = array([1, 2, 4, 5, 6], float)  # it will make an int array
# arr = array([1, 2, 4, 5, 6.1], int) # it will make an int array
# arr = array([1, 2, 4, 5, 6])
# print(arr)
# print(arr.dtype)  # it will give the type of array


# 2. linspace()
# arr2 = linspace(0, 15, 16) # it will divide range(0,15) into 16 parts
# print(arr2)

# arr3 = linspace(0,15) # if we dont mention the third argument,by default it will divide into 50 parts
# print(arr3)

# 3. arange()
# arr4 = arange(0,15,2) # third arguments is step
# print(arr4)

# 4. logspace()
# arr5 = logspace(1,40,5)
# print(arr5)
# print('%.2f' %arr5[4])

# 5. zeros()
# arr6 = zeros(5) # it will create an array of size 5 with each element 0.
# print(arr6)

# 6. ones()
arr7 = ones(5) # it will create an array of size 5 with each element 1.
print(arr7)


