class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input(
                """\nHello, how would you like to proceed?
1. Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit
"""
            )
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye!")
                break
            else:
                print("Invalid input. Try again.")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin Set Successfully")

    def deposit(self):
        temp = input("Enter your Pin: ")
        if temp == self.pin:
            amount = int(input("Enter the Amount: "))
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your Pin: ")
        if temp == self.pin:
            withdraw_amount = int(input("Enter The Withdraw Amount: "))
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print("Operation Successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your Pin: ")
        if temp == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid Pin")


# Start the program
Atm()
