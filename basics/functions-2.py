# in python we dont use pass by value or pass by reference


# def update(x):
#     print(id(x))
#     x = 8
#     print(id(x))
#     print("updated value", x)
#
# y = int(input("Enter any value to update "))
# print(id(y))
# update(y)
# print("enetered value", y)


def update(lst):
    print(id(lst))
    lst[1] = 356
    print(id(lst))
    print("lst ",lst)


lst = [10, 20, 30, 40]
print(id(lst))
update(lst)
print("lst = ",lst)
