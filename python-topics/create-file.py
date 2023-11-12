"""
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

"""
# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Create a new file if it does not exist:
f = open("myfile.txt", "w")