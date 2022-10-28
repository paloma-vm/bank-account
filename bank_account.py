# Bank Account assignment

class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number =  account_number
        self.balance =  balance

    # methods
    def deposit(self, amount):
        new_balance = balance + amount
        
        print(f"Amount deposited: ${amount} new balance: ${balance}")
