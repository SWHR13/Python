text = input("Enter a string: ")
if text.isdigit():  # isdigit()is used to check digits in the string.
    print(f"{text} contains only digits.")
else:
    print(f"{text} does not contain only digits")
