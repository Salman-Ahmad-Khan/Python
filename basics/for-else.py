# nums = [20, 53, 98, 37, 23]
# for num in nums:

for num in range(1, 20):
    if num % 5 == 0:
        print(num)
        break  # if we want only first number,put break
else:
    print("Not Found")
