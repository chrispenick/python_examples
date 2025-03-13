class BankAccount:
    """
    A class representing a simple bank account with property decorators.
    """
    
    def __init__(self, account_holder, account_number, balance=0):
        """
        Initialize a new bank account.
        
        Args:
            account_holder (str): Name of the account owner
            account_number (str): Unique account identifier 
            balance (float, optional): Starting balance. Defaults to 0.
        """
        self._account_holder = account_holder  # Note the underscore prefix
        self._account_number = account_number  # Indicates these are "private" attributes
        self._balance = balance
        self._transaction_history = []
    
    @property
    def account_holder(self):
        """Get the account holder's name."""
        return self._account_holder
    
    @account_holder.setter
    def account_holder(self, name):
        """
        Set the account holder's name.
        Name must be at least 2 characters long.
        """
        if len(name) < 2:
            raise ValueError("Account holder name must be at least 2 characters")
        self._account_holder = name
    
    @property
    def account_number(self):
        """Get the account number."""
        return self._account_number
    
    # No setter for account_number - making it read-only after creation
    
    @property
    def balance(self):
        """Get the current account balance."""
        return self._balance
    
    # No direct setter for balance - can only change through deposit/withdraw
    
    @property
    def transaction_history(self):
        """Get a copy of the transaction history."""
        # Return a copy to prevent external modifications
        return self._transaction_history.copy()
    
    def deposit(self, amount):
        """
        Add money to the account balance.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            float: Updated account balance
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
            
        self._balance += amount
        self._transaction_history.append(f"Deposit: +${amount}")
        return self._balance
    
    def withdraw(self, amount):
        """
        Remove money from the account balance if sufficient funds exist.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            float: Updated account balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
            
        if amount > self._balance:
            raise ValueError("Insufficient funds")
            
        self._balance -= amount
        self._transaction_history.append(f"Withdrawal: -${amount}")
        return self._balance
    
    def __str__(self):
        """Control how the object is represented as a string."""
        return f"Account({self._account_holder}, ${self._balance})"