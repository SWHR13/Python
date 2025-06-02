"""
A function is a block of code which only runs when it is called.
We can pass data,known as parameters,into a function.
A function can return data as a result.
"""

# Calling a Function
# A function can be created by using (def) keyword.


def myfunction():
    print("hello")


myfunction()  # function calling.
# To call a function we use function name followed by parenthesis.

# ARGUMENTS
"""
(Information can be passed into function as arguments)
Arguments are specified after the function name,inside the parenthesis.We can add as many arguments as we want,just seperate them with a comma.
"""


def my_function(fname):  # fname is the parameter
    print(fname + " " + "hussain")


my_function("Wali")  # Wali is an argument
my_function("Ali")  # Ali is an argument

"""
    | **Term**  | **Where it shows**                      |
| --------- | --------------------------------------- |
| Parameter | In the function **definition** (header) |
| Argument  | In the function **call**                |

"""

# NO.Of ARGUMENTS
"""
By default,a function must be called with the correct number of arguments.Meaning that if your function expects 2 arguments,you have to call the function with 2 arguments,nt more or less than 2.
"""


def func(fname, lname):  # fname,lname is the parameter
    print(fname + " " + lname)


func("Wali", "Rizvi")  # Wali is an argument
func("Ali", "Rizvi")  # Ali is an argument

# ARBITRARY ARGUMENTS,*args
"""
If you do not know how many arguments that will be passed into the functions,add * before the parameter name in the function definition.
It collects extra positional arguments into a tuple
"""


def child(*kids):
    print(f"The Youngest Child is {kids[2]}")


child("Wali", "Hasan", "Yaseen")

# KEYWORD ARGUMENTS
"""
You can also send arguments with the "key=value" syntax.In this way the order of arguments does not matter
"""


def children(child1, child2, child3):
    print(f"The Youngest daughter is {child1}")


children(child1="Ailiya", child2="Maham", child3="Meerub")


# Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
# If the number of keyword arguments is unknown, add a double ** before the parameter name:


def my_function(**kid):
    print("His last name is " + kid["lname"])


# DEFAULT PARAMETER
my_function(fname="Tobias", lname="Refsnes")

"""The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:
"""


# Example
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
"""
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function:
Example
"""


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values
# To let a function return a value, use the return statement:


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.


def myfunction():
    pass


# Positional-Only Arguments
"""You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:
"""


def my_function(x, /):
    print(x)


my_function(3)


# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
    print(x)


my_function(x=3)
# But when adding the , / you will get an error if you try to send a keyword argument:


# keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:


def my_function(*, x):
    print(x)


my_function(x=3)
# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:


def my_function(x):
    print(x)


my_function(3)
# But with the *, you will get an error if you try to send a positional argument:


def my_function(*, x):
    print(x)


# my_function(3)

# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.


def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)


# Recursion
"""
#Python also accepts function recursion, which means a defined function can call itself.

#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
"""


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)
