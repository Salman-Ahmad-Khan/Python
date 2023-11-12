# x = input("Enter the 1st number") # input() gives us string
x = int(input("Enter the 1st number"))
# a = int(x) #converted string into an int
y = int(input("Enter the 2nd number"))
# b = int(y)
z = x + y
print("The sum:", z)


""" to take a string and print a specific character of string  """
ch = input('Enter any string') [0]
print(ch)
# print('The character is', ch[0]) """ to print one chracter we use index number, in this case ch[0] """



# to evaluate any mathamatical expression we can use  eval() function
result = eval(input('Enter any expression'))
print(result)