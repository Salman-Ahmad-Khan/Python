# to take the input from command prompt we use a module called 'sys' and use a function called 'argv'


import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(z)
