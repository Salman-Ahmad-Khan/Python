# to use arrays and its corresponding functions we have to first import it
# import array as arr
# import array
from array import *   # '*' will import all the functions from 'array module'
vals = array('i', [5, 2, 1, -7, 9, 3, 4]) # array.array(typecode,[initializer])
# print(vals)
#
# vals.reverse()
# print(vals)
#
# print(vals.buffer_info())   #it will print the address and size of array
# print(vals.typecode)  # it will print the typecode of array

# print(vals[0])   # it will print first element of array

# this will print array elements one by one
# for i in vals:
#     print(i)

# aliter
# for i in range(7):
#     print(vals[i])

# aliter
# for i in range(len(vals)):
#     print(vals[i])


# character array
# ch = array('u', ['a', 'e', 'i'])
# print(ch)

# for i in range(3):
# for i in range(len(ch)):
#     print(ch[i])


# copy an array
# newary = array(vals.typecode, (a for a in vals))
newary = array(vals.typecode, (a*a for a in vals))   # the 'newary' will be the sqaure of 'vals' array
# print("copied array: ", newary)

# using for loop
# for i in newary:
#     print(i)

# using while loop
i = 0
while i <= 6:  # while i < len(newary):
    print(newary[i])
    i = i+1













