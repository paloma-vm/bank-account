# Bank Account assignment
import random

# def create_account():
# # **kwargs?
#         full_name = ''
#         account_number = random.randint(10000000, 99999999)
#         balance = float (0)
#         # return user_account.dict 
#         # return self.dict


class BankAccount:
    def __init__(self, full_name, account_number=random.randint(10000000, 99999999), balance=float(0)):
        self.full_name = full_name
        self.account_number = account_number
        self.balance =  balance

    # methods
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        # Got help from this source: https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
        self.balance += amount
        # ?? balance += amount
        print(f"\n Amount deposited: ${amount}  new balance: ${self.balance}")
        

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ")) 
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}  new balance: ${self.balance}')
        else:
            print("Insufficient funds.")
            overdraft_fee = float(10)
            self.balance -= overdraft_fee

    def get_balance(self):
        print(f'Your current account balance is: ${self.balance}')
        return self.balance

    def add_interest(self):
        monthly_interest = self.balance * 0.083
        self.balance += monthly_interest
        return self.balance
    
    # the reference I am using to make a print_statement method
        # for key, value in self.items():
        #     print(key + ': ' + str(value))
    def print_statement(self):
        display_account_no = self.account_number.range(0, 4)
        print(f'{self.full_name}\nAccount No.: {display_account_no}****\nBalance: ${self.balance}')

# define 3 bank account examples
account_1 = BankAccount("Sparky Jones", 12345678, 2000.00)
print(account_1.__dict__)


# add docstrings



