x = int(input('Enter any number:  '))
r = x % 2
if (r == 0):
    print('EVEN')
    if (x > 3):
        print("Greater tha 3")
    else:
        print("not greater than 3")
else:
    print('ODD')
