try:
    numerator = int(input("Enter the Numerator: "))
    denominator = int(input("Enter the Denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("You cannot divide by 0")
except ValueError:
    print("Error:Invalid input,please enter a valid input: ")
else:
    print(f"Result: {result}")
finally:
    print("Execution Completed!")
