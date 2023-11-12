num = 9.5
print(num)
print(type(num))


b = 5 + 6j
print(b)
print(type(b))


n = 22.13
print(n,type(n))

# Python allows us to change data types
b = 6.25
print(b)
print(type(b))
print(int(b))

c = 56
print(float(c))

print("The complex of b and c :", complex(b, c))

d = 45
h = 65
print(d>h)
print(h>d)

print("The integer of True is:", int(True))
print("The float of true is:", float(True))
print(type(True))

print("The integer of False is:", int(False))
print("The float of False is:", float(False))
print(type(False))



o = {'salman':'samsung','jack':'redmi','roomi':'realme'}


print(o)
print(o.get('salman'),o.get('jack'))