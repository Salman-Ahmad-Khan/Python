# def greet():        # defining a function
#     print("Hii...")
#     print("Good Morning ❤")

# greet()             # calling a function
# greet()

# x = int(input())
# y = int(input())
# def add(x, y):
#     c = x + y
#     return c  # it will return to, where the function is called

# ans = add(x,y)   # assigning return value
# print("Addition of",x,"and",y,"is",ans)


# make a function that can add and subtract two numbers simultaneously

def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d  # it will return two values,where the function is called


ans1, ans2 = add_sub(2, 8)  # assigning 'return' values
print(ans1,"is the addition", "and", ans2, "is the subtraction")  # printing addition and subtraction
