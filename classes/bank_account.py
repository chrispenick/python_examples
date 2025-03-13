class BankAccount:
    """
    A class representing a simple bank account.
    """
    
    def __init__(self, account_holder, account_number, balance=0):
        """
        Initialize a new bank account.
        
        Args:
            account_holder (str): Name of the account owner
            account_number (str): Unique account identifier 
            balance (float, optional): Starting balance. Defaults to 0.
        """
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []  # Empty list to store transaction records
    
    def deposit(self, amount):
        """
        Add money to the account balance.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            float: Updated account balance
        """
        if amount <= 0:
            print("Deposit amount must be positive")
            return self.balance
            
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return self.balance
    
    def withdraw(self, amount):
        """
        Remove money from the account balance if sufficient funds exist.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            float: Updated account balance
        """
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return self.balance
            
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
            
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount}")
        return self.balance
    
    def get_balance(self):
        """
        Check the current account balance.
        
        Returns:
            float: Current balance
        """
        return self.balance
    
    def view_transaction_history(self):
        """
        Display all transactions made with this account.
        
        Returns:
            list: List of transaction records
        """
        return self.transaction_history