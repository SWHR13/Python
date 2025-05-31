number = list(map(int, input("Enter the List of number with spaces: ").split()))
sum_even = sum(num for num in number if num % 2 == 0)
print(f"The sum of Even Numbers is: {sum_even}")

# Logic:
"""
    | Step | Code Part       | What it does                | Result                   |
| ---- | --------------- | --------------------------- | ------------------------ |
| 1    | `input(...)`    | Takes user input            | `"10 5 8 21"`            |
| 2    | `.split()`      | Splits the string           | `["10", "5", "8", "21"]` |
| 3    | `map(int, ...)` | Converts each string to int | `10, 5, 8, 21`           |
| 4    | `list(...)`     | Makes a list from that      | `[10, 5, 8, 21]`         |

"""
