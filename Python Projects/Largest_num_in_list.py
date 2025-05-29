number = list(map(int, input("Enter the numbers with spaces: ").split()))
largest = max(number)
print(f"The Largest number in the List is: {largest}")

# Logic:
"""
    | Step | Code Part       | What it does                | Result                   |
| ---- | --------------- | --------------------------- | ------------------------ |
| 1    | `input(...)`    | Takes user input            | `"10 5 8 21"`            |
| 2    | `.split()`      | Splits the string           | `["10", "5", "8", "21"]` |
| 3    | `map(int, ...)` | Converts each string to int | `10, 5, 8, 21`           |
| 4    | `list(...)`     | Makes a list from that      | `[10, 5, 8, 21]`         |

"""
