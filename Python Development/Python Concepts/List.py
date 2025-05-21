"""
List are used to store multiple items in a single variable.List are creatrd using[] brackets.
List items are ordered,changeable and allow duplicate values. (Order can't change).
If we add new item,it will placed at the last of the list
"""
# List Length
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(list))

"""
List can store any data type like int,bool,string or it can store multiple variables of different datatypes in a single list
Like list=["ali",1,True]
"""

# Accessing List Item
list = ["apple", "mango", "orange", "guava", "peach", "berry"]
print(list[1])  # print second item of the list
print(list[2:5])  # print items through the range of indexes

# Changing List Item
list[1] = "banana"  # Changing second item of the list
print(list)

list[1:3] = "strawberry", "watermelon"  # Adding fruits by the range of indexes
print(list)

# Change the second value by replacing it with two values
list[1:2] = ["cherry", "banana"]
print(list)

# Change Second and third value by replacing it with one value
list[1:3] = ["avagado"]
print(list)

# Insert Items
"""
to insert any new item without replacing the others,we can use Insert() method
"""
numbers = [1, 2, 3, 4, 5]
# it means that on 2nd index,10 will be added into the list
numbers.insert(2, 10)
print(numbers)

# Add List Item
veg = ["potato", "onion", "tomato", "lemon"]
veg.append("carrot")  # append is used to insert a new item at last
print(veg)

# To add an item on a specified index,
odd = [1, 3, 5, 7, 9]
odd.insert(1, 11)  # Insert is used to add item on a specified index in a list
print(odd)

# Extend List
list10 = [1, 3, 5, 7, 9, 5]
list20 = [2, 4, 6, 8, 10]
# To append elements from another list to the current list, use the extend() method.
list10.extend(list20)
print(list10)

# Remove List Item
list10.remove(5)  # Remove() removes the element from the list
# if there are more than one same element in the list,it will only remove the first one
print(list10)

# Remove Specific Index

# To remove the specific index,use pop().
list10.pop(1)
print(list10)

# del is similar to pop
del list10[5]
print(list10)

# clear is used to clear all the elements in the list,but the list will remain there itself
list20.clear()
print(list20)

# SORT LISTS.
"""
List have a sort() method that will sort the list alphanumerically,ascending by default
"""
a = ["apple", "banana", "mango", "avagado"]
b = [19, 3, 45, 56, 9]
a.sort()
b.sort()
print(a)
print(b)

# Sort DESCENDING
b.sort(reverse=True)
print(b)

# CUSTOMIZE SORT FUNCTION
"""
We can customize the function by using the keyword argument "key=argument(function).
The function will return a number that will be used to sort he list (the lower number first)
"""
# Question: Sort the list based on how close the number is to 50:;


def myfunc(n):
    return abs(n-50)


num = [100, 67, 87, 3, 99]
num.sort(key=myfunc)
# num.sort(reverse=True)    Good One WALI!!
print(num)

# EXPLANATION
"""
define function where n is the number,abs() is used to give positive number then we will give a list.
num.sort then sorting the number closest to 50 by subtracting n-50 like 100 is the first element so 100-50=50 ,67-50=17 , 87-50=37 ,3-50=47 ,99-50=49
so we saw that the closest numbers are 17,37,47,49,50 respectively so the answer is (67,87,3,99,100)
"""

# CASE INSENSITIVE SORT
# the sort is case sensitive by default,resulting in all capital letters being sorted before lower case letters:
name = ["wali", "Hussain", "Zohaib", "ahmed"]
name.sort()
print(name)  # ['Hussain', 'Zohaib', 'ahmed', 'wali']

# To make it sequence wise first we have to make the list in lower case
name.sort(key=str.lower)
print(name)  # ['ahmed', 'Hussain', 'wali', 'Zohaib']

# Reverse Order
name.reverse()  # Reverse() is used to reverse the current sorting order of the element
print(name)

# Copy-List
name = name.copy()  # to copy the list,use copy().
print(name)

# Join-List
c1 = [10, 20, 30, 40]
c2 = [50, 60, 70, 80]
c3 = c1+c2
print(c3)

# Also we can use extend() method to add second list to the first one
c1.extend(c2)
print(c1)
