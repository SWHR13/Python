text = input("Enter a string: ")
if (
    text.isalnum()
):  # isalnum() is a python built-in function used to check whether a string is Alphanumeric or not.
    print(f"{text} is AlphaNumeric.")
else:
    print(f"{text} is not AlphaNumeric.")
