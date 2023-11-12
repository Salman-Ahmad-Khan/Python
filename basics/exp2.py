user1 = input("Enter your points:user1\n")
user2 = input("Enter your points:user2\n")
user3 = input("Enter your points:user3\n")
if (user1>user2) and (user1>user3):
    print("User One scored highest points!")
elif (user2>user1) and (user2>user3):
    print("User Two scored highest points!")
else:
    print("User Three scored highest points!")