number = input("Enter a number: ")
if number == number[::-1]:  # reverses the string   (start:stop:end)
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
