import random

low = int(input("Enter the Lowest Number: "))
high = int(input("Enter the Highest Number: "))

random_number = random.randint(low, high)
print(f"The Random number between {low} and {high} is: {random_number}")
