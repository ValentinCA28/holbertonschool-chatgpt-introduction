#!/usr/bin/env python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            print(f"Current Balance: ${self.balance:.2f}\n")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}\n")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}\n")


def get_positive_float(prompt):
    """
    Helper function to safely read a positive number from user.
    Returns the float value or None if input is invalid/cancelled.
    """
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("No input received. Try again.\n")
                continue

            amount = float(value)
            if amount <= 0:
                print("Please enter a positive number.\n")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter a valid number (e.g. 50.25).\n")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None


def main():
    cb = Checkbook()
    print("Welcome to your checkbook!\n")

    while True:
        action = input(
            "What would you like to do? "
            "(deposit / withdraw / balance / exit): "
        ).strip().lower()

        if action in ('exit', 'quit', 'q'):
            print("Goodbye!\n")
            break

        elif action == 'deposit':
            amount = get_positive_float("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)

        elif action == 'withdraw':
            amount = get_positive_float("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()

        elif action == '':
            print("No command entered. Try again.\n")

        else:
            print("Invalid command. Please choose from: deposit, withdraw, balance, exit\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("The checkbook program has stopped.")
