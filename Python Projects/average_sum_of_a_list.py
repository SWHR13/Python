num = list(map(int, input("Enter the List of numbers with spaces: ").split()))
average = sum(num) / len(num)
print(f"The average of the numbers is: {average}")


"""    | Step | Code Part       | What it does       
| ---- | --------------- | --------------------------- 
| 1    | `input(...)`    | Takes user input            
| 2    | `.split()`      | Splits the string           
| 3    | `map(int, ...)` | Converts each string to int 
| 4    | `list(...)`     | Makes a list from that      

"""
