"""
Use a Module
Now we can use the module we just created, by using the import statement:

Example
Import the module named mymodule, and call the greeting function:


Note: When using a function from a module, use the syntax: module_name.function_name.
"""
import module

module.greeting("Salman")


"""
Example
Import the module named module, and access the person1 dictionary:
"""
a = module.person1["age"]
print(a)


"""
Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

Example
Create an alias for module called salmans-module:
"""
import module as salman

a = salman.person1["age"]
print(a)



"""
Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.

Example
Import and use the platform module:
"""
import platform

x = platform.system()
print(x)


"""
Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

Note: The dir() function can be used on all modules, also the ones you create yourself.

Example
List all the defined names belonging to the platform module:

"""
import platform

x = dir(platform)
print(x)


"""
Import From Module
You can choose to import only parts from a module, by using the from keyword.

Example
The module named mymodule has one function and one dictionary:
Example
Import only the person1 dictionary from the module:


Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not module.person1["age"]
"""
from module import person1

print (person1["country"])


