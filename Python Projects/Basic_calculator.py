print("Hello! Welcome to the Basic Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Choose an Operation (1/2/3/4): ")  # Selecting Operation

# Validity Check (if we don't add this line of code,Every letter or number will continue the operations of calculator)
if choice in ("1", "2", "3", "4"):
    num1 = float(input("Enter first number: "))  # First User Input
    num2 = float(input("Enter second number: "))  # Second User Input

if choice == "1":
    print(f"The result of the Addition is {num1+num2}")
elif choice == "2":
    print(f"The result of the Subtraction is {num1-num2}")
elif choice == "3":
    print(f"The result of the Multiplication is {num1*num2}")
elif choice == "4":
    if num2 != 0:
        print(f"The result of the Division is {num1/num2}")
    else:
        print("Operation is not possible")
else:
    print("Enter a Valid Number")
