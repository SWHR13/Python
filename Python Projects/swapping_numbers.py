a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = b, a  # Now a holds the value of b and b holds the value of a.
print(f"After swapping: a= {a} , b={b}")
