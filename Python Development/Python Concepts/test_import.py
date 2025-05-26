# import mymodule
# a = mymodule.person1["age"]
# print(a)

# Renaming a module
from mymodule import person1
import platform
import mymodule as mx
a = mx.person1["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
x = platform.system()
print(x)

"""Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
"""
x = dir(platform)
print(x)

#from mymodule import person1
print(person1["age"])
