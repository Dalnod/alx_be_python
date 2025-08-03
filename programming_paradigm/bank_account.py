class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        # Not used anymore, but kept for compatibility
        print(f"Current Balance: ${int(self.account_balance) if self.account_balance == int(self.account_balance) else self.account_balance}")
        