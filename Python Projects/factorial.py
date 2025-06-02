"""
Dry Run (when input = 4)
User Input
num = 4

Calling factorial(4)

n = 4 → Not 0 or 1 → Return 4 * factorial(3)

Calling factorial(3)

n = 3 → Not 0 or 1 → Return 3 * factorial(2)

Calling factorial(2)

n = 2 → Not 0 or 1 → Return 2 * factorial(1)

Calling factorial(1)

n = 1 → Return 1 (Base case)
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter the number: "))
print(f"The factorial of a {num} is {factorial(num)}.")


# OR
"""
import math
print(math.factorial(5))
"""
