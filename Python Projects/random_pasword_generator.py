import string
import random

length = int(input("Enter the Password Length: "))
characters = string.ascii_letters + string.digits
password = "".join(random.choices(characters, k=length))
print(f"Generated password: {password}")

"""random.choices(characters, k=length) → picks length number of random characters from characters.

"".join(...) → joins them with spaces between (so the password will look like a B 3 Z q 9).

"""
