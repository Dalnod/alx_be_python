import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${int(amount) if amount == int(amount) else amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${int(amount) if amount == int(amount) else amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        print(f"Current Balance: ${int(account.account_balance) if account.account_balance == int(account.account_balance) else account.account_balance}")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()