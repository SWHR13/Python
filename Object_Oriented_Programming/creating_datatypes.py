# Visit: Magic Methods in Python
class Fraction:
    def __init__(self, numerator, denominator):

        if denominator == 0:
            raise ValueError("Denominator can't be 0")
        self.num = numerator
        self.den = denominator

    # String
    def __str__(self):
        return f"{self.num}/{self.den}"  # The __str__ method makes your Fraction objects print in a friendly way (like "1/2") instead of a confusing default (like <object at 0x...>).

    # Addition
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(
            temp_num, temp_den
        )  # "{}/{}": These are "placeholders" within the string. The first {} will be replaced by the first value provided to format(), and the second {} by the second value.

    # Subtraction
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    # Multiplication
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    # Division
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)


# --- Example Usage ---
if __name__ == "__main__":
    # Create some fraction objects
    fraction1 = Fraction(1, 2)  # 1/2
    fraction2 = Fraction(3, 4)  # 3/4
    fraction3 = Fraction(5, 3)  # 5/3
    fraction4 = Fraction(0, 5)  # 0/5

    print(f"Fraction 1: {fraction1}")
    print(f"Fraction 2: {fraction2}")
    print(f"Fraction 3: {fraction3}")
    print(
        f"Fraction 4: {fraction4}\n"
    )  # \n adds a new line (a blank line in this case) to the output, which helps to make the printed information easier to read by creating visual separation.

    # Perform operations as shown in the image
    print(f"Addition (1/2 + 3/4): {fraction1 + fraction2}")
    print(f"Subtraction (1/2 - 3/4): {fraction1 - fraction2}")
    print(f"Multiplication (1/2 * 3/4): {fraction1 * fraction2}")
    print(f"Division (1/2 / 3/4): {fraction1 / fraction2}")

    try:
        print(
            f"Division (1/2 / 0/5): {fraction1 / fraction4}"
        )  # This will raise an error
    except ValueError as e:
        print(f"Error for division by zero numerator: {e}")


# USER INPUT
""""
def get_fraction_input(fraction_name):
    while True:
        try:
            print(f"\nEnter details for {fraction_name}:")
            num = int(input(f"Enter numerator for {fraction_name}: "))
            den = int(input(f"Enter denominator for {fraction_name}: "))
            return Fraction(num, den)
        except ValueError as e:
            print(
                f"Invalid input: {e}. Please enter integer values and a non-zero denominator."
            )
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


if __name__ == "__main__":
    print("--- Fraction Calculator ---")

    fraction1 = get_fraction_input("Fraction 1")
    fraction2 = get_fraction_input("Fraction 2")
    fraction3 = get_fraction_input("Fraction 3")

    fraction4 = Fraction(0, 5)

    print("\n--- Your Fractions ---")
    print(f"Fraction 1: {fraction1}")
    print(f"Fraction 2: {fraction2}")
    print(f"Fraction 3: {fraction3}")
    print(f"Fraction 4 (hardcoded 0/5 for testing): {fraction4}\n")

    print("--- Arithmetic Operations ---")
    print(f"Addition ({fraction1} + {fraction2}): {fraction1 + fraction2}")
    print(f"Subtraction ({fraction1} - {fraction2}): {fraction1 - fraction2}")
    print(f"Multiplication ({fraction1} * {fraction2}): {fraction1 * fraction2}")
    print(f"Division ({fraction1} / {fraction2}): {fraction1 / fraction2}")

    try:
        print(f"Division ({fraction1} / {fraction4}): {fraction1 / fraction4}")
    except ValueError as e:
        print(f"Caught error: {e}")
"""
