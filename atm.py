class ATM:
    def __init__(self):
        self.pin = "1234"
        self.balance = 5000

    def login(self):
        attempts = 3

        while attempts > 0:
            entered_pin = input("Enter your 4-digit ATM PIN: ")

            if entered_pin == self.pin:
                print("\nLogin Successful!")
                return True
            else:
                attempts -= 1
                print("Incorrect PIN!")
                print("Attempts remaining:", attempts)

        print("\nYour account is temporarily locked.")
        return False

    def check_balance(self):
        print("\nYour current balance is: Rs.", self.balance)

    def deposit(self):
        amount = float(input("\nEnter amount to deposit: Rs. "))

        if amount > 0:
            self.balance += amount
            print("Deposit Successful!")
            print("Updated Balance: Rs.", self.balance)
        else:
            print("Please enter a valid amount.")

    def withdraw(self):
        amount = float(input("\nEnter amount to withdraw: Rs. "))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: Rs.", self.balance)

        else:
            print("Insufficient Balance!")

    def menu(self):
        while True:
            print("\n========== ATM MENU ==========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("==============================")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("\nThank you for using our ATM!")
                break

            else:
                print("Invalid choice! Please select between 1 and 4.")


atm = ATM()

print("================================")
print("       WELCOME TO PYTHON ATM")
print("================================")

if atm.login():
    atm.menu()
