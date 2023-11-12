from numpy import *

# matrx = array([[1,2,3],[4,5,6]])
# or
#  matrx = array([
#             [1,2,3,5,2,1],
#             [4,5,6,3,7,1]
#              ])
# print(matrx)
# print(matrx.dtype)
# print(matrx.ndim)       # it will give dimension
# print(matrx.shape)      # it will give the order of matrix i.e number of rows ans columns
# print(matrx.size)         # it will give the size i.e number of elements

# matrx1 = matrx.flatten()    # it will convert multi-dimensional matrix to 1-D
# print(matrx1)

# matrx1 = array([1, 2, 3, 5, 2, 1, 4, 5, 6, 3, 7, 1])
# it is a 1-D array
# matrx3 = matrx1.reshape(3,4)  # it will convert 1-D into multi-D, (we have to define rows and columns)
# print(matrx3)

# martx2 = matrx1.reshape(2,2,3)  # it will create two 2-D arrays of order 2x3
# print(martx2)


# another way of creating matrices
m = matrix('1,2,3; 5,2,4; 5,0,3')
# print(m)
# print(diagonal(m),"are diagonal elements of m")
# print(m.min()) # it will give the smallest element
# print(m.max()) # it will give the largest element

m1 = matrix('1,7,3; 5,2,4; 5,9,0')
# m3 = m1 + m   # adding two matrices
# print(m3)
m4 = m * m1     # multiplying two matrices
print(m4)

