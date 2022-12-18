import sys

class Customer:
    '''Banking application to perform some task'''
    bank_name = 'kotak'

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'balance after deposit is:{self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('insufficient balance please update your balance!!!')
            sys.exit(0)

        else:
            self.balance = self.balance - amount
            print(f'balance after withdraw:{self.balance}')

    def check_balance(self):
        print(f'the account balance is:{self.balance}')

if __name__ == '__main__':
    print(f'welcome to {Customer.bank_name} bank application')
    name = input('enter the name of the customer:\t')

    ref = Customer(name=name, balance=0.0)
    while True:
        print("select your option:\t d/D-Deposit\t w/W-withdraw\t c/C-check_balance\t e/E-Exit")
        option = input("enter your option:\t")

        if option == 'd' or option == 'D':
            amount = int(input("enter the deposit amount:\t"))
            ref.deposit(amount)

        elif option == 'w' or option == 'W':
            amount = int(input("enter the withdraw amount:\t"))
            ref.withdraw(amount)

        elif option == 'c' or option == 'C':
            ref.check_balance()

        elif option == 'e' or option == 'E':
            print(f'thank you for using {Customer.bank_name} application')
            sys.exit(0)

        else:
            ('invalid option... plz try again...')
        