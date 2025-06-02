num = int(input("Enter the numbers: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print(f"Sum of Digits: {sum_of_digits}")

"""
    sum_of_digits = sum(int(digit) for digit in str(num))
Here's what happens step by step:

str(num) → converts the number (like 123) into a string '123' so we can loop through each character.

for digit in str(num) → loops over each character ('1', '2', '3').

int(digit) → converts each character back to an integer (1, 2, 3).

sum(...) → adds them all together (1 + 2 + 3 = 6).

 """
