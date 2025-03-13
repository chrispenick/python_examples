from bank_account_props import BankAccount

# Creating a bank account
try:
    # Create an account
    alice_account = BankAccount("Alice Smith", "AC001", 1000)
    
    # Using properties to access attributes
    print(f"Account Holder: {alice_account.account_holder}")
    print(f"Account Number: {alice_account.account_number}")
    print(f"Current Balance: ${alice_account.balance}")
    
    # Using property setter
    alice_account.account_holder = "Alice Johnson"  # Changed after marriage
    print(f"Updated Account Holder: {alice_account.account_holder}")
    
    # Attempting to change account number (should fail)
    try:
        alice_account.account_number = "AC999"
        print("Account number changed (this shouldn't happen)")
    except AttributeError as e:
        print(f"Cannot change account number: {e}")
    
    # Making transactions
    alice_account.deposit(500)
    alice_account.withdraw(200)
    
    # Checking balance and history using properties
    print(f"New Balance: ${alice_account.balance}")
    print("Transactions:", alice_account.transaction_history)
    
    # Demonstrating proper validation
    try:
        alice_account.deposit(-100)
    except ValueError as e:
        print(f"Error: {e}")
        
    try:
        alice_account.withdraw(5000)
    except ValueError as e:
        print(f"Error: {e}")
        
    # Demonstrating invalid name change
    try:
        alice_account.account_holder = ""
    except ValueError as e:
        print(f"Error: {e}")
        
except Exception as e:
    print(f"Unexpected error: {e}")