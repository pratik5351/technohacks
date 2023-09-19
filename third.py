class BankAccount:
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        return self.balance


def main():
    print("WELCOME TO STATE BANK")
    account_number = int(input("Enter your account number: "))  # Convert input to an integer
    pin = int(input("Enter your PIN: "))  # Convert input to an integer

    # Create a bank account instance
    account = BankAccount(account_number, pin)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Your balance is:", account.check_balance())
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if account.deposit(amount):
                print("Deposit successful. New balance:", account.check_balance())
            else:
                print("Invalid deposit amount.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if account.withdraw(amount):
                print("Withdrawal successful. New balance:", account.check_balance())
            else:
                print("Insufficient balance or invalid amount.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
