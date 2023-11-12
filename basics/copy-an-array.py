from numpy import *
# copying an array
# arr1 = array([1, 2, 3, 8, 9])
# arr2 = arr1   # Aliasing, by this way we will have two arrays with same elements and same  address(id),
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))


# arr3 = array([1, 2, 3, 8, 9])
# arr4 = arr3.view()
# arr3[1] = 51
"Shallow copy --it will reflect to both the arrays, it will create a new array with  elements same as arr3 but with a different  address(id)"
# print(arr3)
# print(arr4)
# print(id(arr3))
# print(id(arr4))

arr3 = array([1, 2, 3, 8, 9])
arr4 = arr3.copy()
arr3[1] = 51
"Deep copy --it will reflect to  the arr3 only   it will create a new array with  elements same as arr3 but with a different  address(id)"

print(arr3)
print(arr4)
print(id(arr3))
print(id(arr4))