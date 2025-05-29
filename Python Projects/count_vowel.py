text = input("Enter a string: ")  # Hussain
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"The total vowels in the string is: {count}")

"""

This is the main logic. Let's break it into small steps:

for char in text: go through each letter in the user input.

if char in vowels: check if that letter is a vowel.

1 for ...: for every vowel found, add 1.

sum(...): adds up all the 1s to get the total number of vowels.

"""
