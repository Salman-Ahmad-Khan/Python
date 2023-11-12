# we can import any module as per our defined keywords
"""module name: math
    DESCRIPTION:
    This module provides access to the mathematical functions
    defined by the C standard."""
    
import math as m
print(m.sqrt(625))


# also we can import any specific functions from a module

from math import sqrt,pow,floor,ceil
print("square root of 1024 is ",sqrt(1024))
print("25 raised to power 2 is " ,pow(25,2))
print("The floor value of 5.6 is ",floor(5.6))
print("The ceil value of 5.6 is ",ceil(5.6))