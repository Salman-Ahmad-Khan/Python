# num = 12
num = int(input("Enter any number "))

for i in range(2, num):
    if num % i == 0:
        print("Not a prime")
        break
else:

        print("Prime")