a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    a, b = (
        b,
        a,
    )  # The Condition will swap if it runs correctly (the value of b will place in variable a and the value of a will place in variable b )
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print("Sorted numbers are: ", a, b, c)
