class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        print(f'Deposited:{amount}')

    def withdraw(self,amount):
        if self.balance < amount:
            print('insufficient balance')
            return
        self.balance-=amount
        print(f'Withdraw: {amount}')
    
    def display_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount()
account.deposit(500)
account.withdraw(200)
account.display_balance()

