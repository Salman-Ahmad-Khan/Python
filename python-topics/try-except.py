"""
Python Try Except
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:


"""
try:
  print(x)
except:
  print("An exception occurred")

"""
Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:
"""

"""
Else
You can use the else keyword to define a block of code to be executed if no errors were raised:
"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

"""
Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.
"""
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

  # This can be useful to close objects and clean up resources:
  try:
    f = open("demofile.txt")
    try:
      f.write("Lorum Ipsum")
    except:
      print("Something went wrong when writing to the file")
    finally:
      f.close()
  except:
    print("Something went wrong when opening the file")


"""
Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.
"""
p = -1

if p < 0:
  raise Exception("Sorry, no numbers below zero")



