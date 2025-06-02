"""
short dry run summary:

Input numbers → split and convert to int → sort them

Find length n

If n is even → median = average of two middle numbers

If n is odd → median = middle number

Print the median

Example:
Input: 7 3 5 1 9 → sorted: [1,3,5,7,9] → odd count → median = 5

"""

numbers = sorted(map(int, input("Enter the numbers seperated by spaces: ").split()))
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    median = numbers[n // 2]

print(f"The median is: {median}")
