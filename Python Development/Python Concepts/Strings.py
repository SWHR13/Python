# Slicing
b = "Hello World"
print(b[2:5])      # first include last exclude

# Slice from the start
b = "Hello World"
print(b[:5])       # Output till index 4

# Slice to the End
b = "Hello World"
print(b[2:])

# Negative Indexing
b = "Hello World"
print(b[-5:-2])

# Modify Strings
a = "Hello World"
print(a.upper())  # CAPITAL
print(a.lower())  # small alphabets
# It removes any blank spaces from the beginning or the end if occurs
print(a.strip())
print(a.replace("H", "J"))  # Replaces H by J
print(a.split(","))  # It splits the text into List ["Hello World"]

# Concatenate String
a = "Hello"
b = "World"
c = a+" "+b
print(c)

# Format Strings (We can't combine strings and numbers so for this we use f-strings)
age = 36
text = f"My Name is John , I am {age} years old"
print(text)

# Dsiplay the price with 2 decimals:
price = 56
result = f"The price of chocolate is {price:.2f} dollars"
print(result)  # 56.00 Answer

# Inside the bracket
money = f"{20*10} rupees"
print(money)
