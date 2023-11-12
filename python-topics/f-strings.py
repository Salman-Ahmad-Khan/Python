"""
"""

"""
When you're formatting strings in Python, you're probably used to using the format() method.

But in Python 3.6 and later, you can use f-Strings instead. f-Strings, also called formatted string literals, have a more succinct syntax and can be super helpful in string formatting.

What are f-Strings in Python?
Strings in Python are usually enclosed within double quotes ("" ) or single quotes (''). To create f-strings, you only need to add an f  or an F before the opening quotes of your string.

For example, "This" is a string whereas f"This" is an f-String.


How to Print Variables using Python f-Strings
When using f-Strings to display variables, you only need to specify the names of the variables inside a set of curly braces {}. And at runtime, all variable names will be replaced with their respective values.

If you have multiple variables in the string, you need to enclose each of the variable names inside a set of curly braces.
The syntax is shown below:
f"This is an f-string {var_name} and {var_name}."

Here's an example.

You have two variables, language and school, enclosed in curly braces inside the f-String.
"""
language = "Python"
school = "freeCodeCamp"
print(f"I'm learning {language} from {school}.")

# How to Evaluate Expressions with Python f-Strings
num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}.")