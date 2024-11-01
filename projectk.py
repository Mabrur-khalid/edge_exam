class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        # Private attribute for balance
        self.__balance = balance  
    
    def deposit(self, amount):
        """Deposits a specified amount to the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw specified amount from the account if sufficient funds are available."""
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        elif amount <= 0:
            print("amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")
    
    def check_balance(self):
        """Returns current balance of the account."""
        print(f"Balance: ${self.__balance:.2f}")
        return self.__balance

# Example usage
account = BankAccount("Rafi", 100.0)
# Deposits $50
account.deposit(50.0)      
# Checks balance  
account.check_balance()       

try:
    # Attempts to withdraw $200
    account.withdraw(200.0)   
except InsufficientFundsError as e:
    print(e)

# Withdraws $50
account.withdraw(50.0)   

# Checking balance:
account.check_balance()       
