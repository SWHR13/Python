import random

# Generating a Random Number between 1 and 10
secret_number = random.randint(1, 10)
print("Hello! Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 10.Can you guess it?")

attempts = 0

while True:
    guess = input("Enter your Guess (or type 'quit' to exit): ")
    if guess.lower() == 'quit':
        print(f"You gave up! The secret number was {secret_number}.")
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Enter a valid number")
        continue

    attempts += 1

    if guess == secret_number:
        print(f"Congratulations!You guess the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too Low!Try Again")
    else:
        print("Too High!Try Again")
