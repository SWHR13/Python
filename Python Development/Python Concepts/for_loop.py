"""
A for loop is used for iterating over a sequence (that is either a list,set,dictionary or a tuple)
With the for loop we can execute a set of statements once for each item in a list,tuple,set etc.
"""
# Print each fruit in a fruit list
fruits = ['apple', 'banana', 'mango']
for x in fruits:
    print(x)

# Looping through a String
"""
Even strings are iterable objects,they contain a sequence of characters
"""
for x in "banana":
    print(x)

# THE BREAK STATEMENT
"""
With the break statement,we can stop the loop before it has looped through all the items
"""
for x in fruits:
    print(x)
    if x == "banana":
        break

# The Continue Statement
"""
With the continue statement,we can stop the current iteration of the loop and continue with the next.
"""
veg = ["potato", "onion", "tomato"]
for x in veg:
    if x == "onion":
        continue
    print(x)  # Except banana exerything will be printed

# The RANGE Function
"""
Range() function returns a sequence of numbers,starting from 0 by default,and increment by 1 (default) and ends at a specified number like:'
"""

for x in range(10):
    print(x)

for a in range(3, 6):
    print(a)

# Increment the sequence with 3
# (2,30,3) here 2 is the starting point,30 is the ending point where 3 at the last is the increment.
for x in range(2, 30, 3):
    print(x)

# ELSE in FOR Loop
for x in range(4):
    if x == 9:
        break
    print(x)
else:
    print("Mentioned number is out of the List")

# NESTED LOOP
"""
A nested loop is a loop inside a loop.The INNER LOOP will be executed one time for each iteration of the OUTER LOOP.
"""
color = ["red", "yellow", "green"]
toys = ["car", "doll"]

for x in color:
    for y in toys:
        print(x, y)
# Above code combines every color with every toy using a nested loop and prints each combination.

# The PASS Statement
"""
FOR loops can't be empty,but if you want to keep it empty so just put pass statement in a block line of code so it will avoid getting an error
"""
for x in range(10):
    pass

