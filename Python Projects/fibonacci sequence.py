n = int(input("Enter the number of terms: "))
# Takes user input (how many Fibonacci numbers to generate) and converts it to an integer.
f1, f2 = 0, 1
# Initializes the first two numbers of the Fibonacci sequence: 0 and 1.
print("Fibonacci Sequence: ")
for _ in range(
    n
):  # Loops n times.(We use _ because we don’t care about the loop index, just the number of iterations.)
    print(f1, end=" ")
    # Prints the current Fibonacci number (f1), staying on the same line (because of end=" ").
    f1, f2 = f2, f1 + f2

"""Updates f1 and f2:
f1 becomes the old f2.
f2 becomes the sum of old f1 + f2.
This shifts forward in the Fibonacci sequence
"""
