'''Bank account class demo'''

# import the BankAccount class from the bank_account module
from classes.bank_account import BankAccount

# Creating two bank account instances
alice_account = BankAccount("Alice Smith", "AC001", 1000)
bob_account = BankAccount("Bob Jones", "AC002")

# Working with Alice's account
print(f"{alice_account.account_holder}'s starting balance: ${alice_account.get_balance()}")
alice_account.deposit(500)
alice_account.withdraw(200)
print(f"New balance: ${alice_account.get_balance()}")
print("Transaction history:", alice_account.view_transaction_history())

# Working with Bob's account
print(f"\n{bob_account.account_holder}'s starting balance: ${bob_account.get_balance()}")
bob_account.deposit(100)
bob_account.withdraw(50)
print(f"New balance: ${bob_account.get_balance()}")
print("Transaction history:", bob_account.view_transaction_history())

# Demonstrating that each account is independent
print("\nAlice and Bob's accounts are separate:")
print(f"Alice's balance: ${alice_account.get_balance()}")
print(f"Bob's balance: ${bob_account.get_balance()}")