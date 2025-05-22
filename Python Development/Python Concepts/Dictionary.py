"""
Dictionaries are used to store data values in KRY:VALUE pair.
A dictionary is a collection which is unordered,changeable  and do not allow duplicates.
It is written with curly brackets,and have keys and values.
"""
thisdict = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    # They do not allow duplicates like can't have 2 items with the same key.In this case the last updated value will get print.
    "year": 9090
}
print(thisdict)

print(len(thisdict))  # Length
print(type(thisdict))  # Type

# Accessing Items:
"""
Access the items of a dictionary by referring to its key name,inside curly brackets:
"""
y = thisdict["model"]  # Model????Corolla
print(y)

# get() can also br used to access the key
x = thisdict.get("brand")
print(x)

# GET KEYS
"""
Keys() method will return a list of all keys in the dictionary
"""
x = thisdict.keys()
print(x)

# The list of keys is a view of the dictionary,meaning that any changes done to the dictionary will be reflected in the Keys list

fruit = {
    "name": "apple",
    "color": "red",
}

a = fruit.keys()
print(a)  # before change

fruit["season"] = "Summer"
print(a)  # after change

# GET VALUES
"""
This will work same like keys but instead of keys we will use Values to get values
"""
b = fruit.values()
print(b)

# GET ITEMS
""" 
The items() method will return each item (value)in a dictionary,as tuples in a list
"""
a = fruit.items()
print(a)

fruit["season"] = "spring"
print(a)

# UPDATE ITEM
thisdict.update({"brand": "Bugati"})
print(thisdict)

# Removing Items:
thisdict.pop("brand")  # Pop is used to remove the items
print(thisdict)

thisdict.popitem()  # PopItem is used to remove the last inserted item
print(thisdict)

# thisdict.clear()  # clear() method empties the dictionary
# print(thisdict)

# del thisdict()    #it will delete the whole dictionary
# print thisdict

# Copy a Dictionary
thisdict = thisdict.copy()
print(thisdict)

# Nested Dictionaries
"""
A dictionary can contain dictionaries,called nested dictionaries.
"""
myfam = {
    "child1": {
        "name": "wali",
        "age": 22
    },
    "child2": {
        "name": "ali",
        "age": 18
    }
}
print(myfam)

# Access Items in Nested Dictionaries
"""
Use the name os the dictionaries,starting with the outer dictionary
"""
print(myfam["child1"]["name"])
