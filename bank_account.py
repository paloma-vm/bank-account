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
    def __init__(self, full_name, account_number=random.randint(0, 10**7), balance=float(0)):
        # randint(10000000, 99999999) had to change from this to allow for account numbers under 10000000
        # randint range from 0 to 10 to the power of n-1 (how many digits you want = n)
        self.full_name = full_name
        self.account_number = str(account_number)
        # is this the correct place to say that account number should be a string?
        # (this allows for account numbers that start with zero)
        # I also need to figure out a way to have numbers that are less than 8 digits to 
        # have leading zeros to make them 8 digits long.  I will do this if I have time.
        self.balance =  balance

    # methods
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        """A method that asks for an amount to deposit and adds it to the balance and then
        displays the amount deposited and the new balance"""
        # Got help from this source: https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
        self.balance += amount
        # ?? balance += amount
        print(f"\n Amount deposited: ${amount:.2f}  new balance: ${self.balance:.2f}")
        

    def withdraw(self):
        """a method that asks for an amount of money, which is subracted from the balance. 
        If there are insufficient funds, an overdraft fee is subtracted from the balance"""
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount:.2f}  new balance: ${self.balance:.2f}')
        else:
            print("Insufficient funds.")
            overdraft_fee = float(10.00)
            self.balance -= overdraft_fee

    def get_balance(self):
        """a method that displays the current balance to 2 decimal places (currency)"""
        print(f'Your current account balance is: ${self.balance:.2f}')
        return self.balance

    def add_interest(self):
        """A method to calculate monthly interest and add it to self.balance, returns self.balance"""
        monthly_interest = self.balance * 0.00083
        self.balance += monthly_interest
        return self.balance
    
    def print_statement(self):
        """A method to display the account info while masking the first 4 digits of the account number"""
        string_account_no = str(self.account_number)
        display_account_no = '*'*(len(string_account_no)-4) + string_account_no[-4:]
        # this replaces the string with '*', except for the last 4 characters
        # source:https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-90.php

        print(f'{self.full_name}\nAccount No.: {display_account_no}\nBalance: ${self.balance:.2f}')

# define 3 bank account examples
account_1 = BankAccount("Sparky Jones", 12345678, 100.00)
account_2 = BankAccount("Jesse Brown", 86753090, 1000.00)
account_3 = BankAccount("Roy Biv", 78808284, 1.25)

# demonstrate that the methods work
# print(account_1.__dict__)
# account_1.print_statement()
# account_1.deposit()
# account_1.get_balance()

# account_2.print_statement()
# account_2.withdraw()
# account_2.get_balance()
# account_2.add_interest()
# account_2.get_balance()

# account_3.print_statement()
# account_3.withdraw()
# account_3.deposit()
# account_3.print_statement()

# include example code for user Mitchell
account_example = BankAccount("Mitchell", "03141592", 0)
# account number must be a string to allow for leading zero
account_example.deposit()
account_example.print_statement()
account_example.add_interest()
account_example.print_statement()
account_example.withdraw()
account_example.print_statement()
