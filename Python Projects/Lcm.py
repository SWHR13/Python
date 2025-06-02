def lcm(x, y):
    greater = max(x, y)
    while True:
        if (
            greater % x == 0 and greater % y == 0
        ):  # This checks if greater is divisible by both x and y. If yes, then it's the LCM.
            return greater
        greater += 1  # If the current value of greater is not divisible by both x and y, we add 1 and check again.


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The LCM of {a} and {b} is: {lcm(a,b)}.")
