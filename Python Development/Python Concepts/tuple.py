"""
Tuple is a collection which is ordered and unchangeable and it can be written with ()
They have a defined order so that the order will not change.
"""
my_tuple = [1, 2, 3]
print(len(my_tuple))

"""
To create a tuple with only one item,we have to add a COMMA after the item,otherwise python will not recognize it as a tuple.
"""

mytuple = ("apple", )
print(type(mytuple))

# ACCESS TUPLE
"""
We can access tuple items by referring to thr index number,inside square brackets.
"""
thistuple = ["apple", "mango"]
print(thistuple[1])

# UPDATE TUPLE
"""
Once a tuple is created,we cannot change its values.
Tuples are immutable but there is a workaround.You can convert the tuple into alist,change the list and convert back into the tuple
"""
x = ("banana", "apple", "pineapple")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

"""
Similarly tuple cant have built in methods like append() to add so we will do the same,covert the tuple into the list,add the item and then convert it back to tuple.
"""
number = (1, 2, 3, 4)
num = list(number)
num.append(5)  # (1,2,3,4,5)
num.remove(4)  # (1,2,3,5)
number = tuple(num)
print(number)

# ADD TUPLE TO A TUPLE
"""
We are allowed to add tuples to tuples,if you want to add one item or more,create a new tuple and add it to the existing tuple
"""

fruits = ("banana", "apple", "mango", "pineapple")
y = ("peach",)
fruits += y  # OR fruits=fruits+y
print(fruits)

# Delete the tuple
del fruits
# print(fruits)  # Output will show error because fruits has been deleted

# UNPACK TUPLES
"""
In python, we are allowed to extract the values into variables.This is called UNPACKING
"""
veg = ("potato", "brinjal", "cucumber", "tomato")
(green, yellow, red, blue) = veg
print(green)
print(yellow)
print(red)
print(blue)

"""
If number of variable is less than no.of values,you can add * to the variable name & the values will be assigned to the variable as a list
"""
(green, *yellow) = veg
print(green)
print(yellow)

# JOIN TUPLES
a = (1, 2, 3)
b = (3, 4, 5)

c = a+b
print(c)

"""
If we want to multiply the content of a tuple for a certain number of time
"""
d = a*5
print(d)
