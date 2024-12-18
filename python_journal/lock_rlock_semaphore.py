import threading 
import time 

class BankAccount:
    def __init__(self,initial_balance=0):
        self.balance = initial_balance
        self.balance_lock = threading.Lock()
        self.log_rlock = threading.RLock()
        self.semaphore = threading.Semaphore(2)

    def deposit(self,amount):
        with self.balance_lock:
            time.sleep(1)
            self.balance+=amount
            with self.log_rlock:
                print(f'Deposited {amount}. current balance {self.balance}.')

    def withdraw(self,amount):
        with self.semaphore:
            with self.balance_lock:
                if self.balance < amount:
                    with self.log_rlock:
                        print(f'your bank balance is insuficient {self.balance}, gareeb')
                else:
                    time.sleep(1)
                    self.balance-=amount
                    with self.log_rlock:
                        print(f'Withdrawed {amount}, current balance {self.balance}')

    def get_balance(self):
        with self.balance_lock:
            with self.log_rlock:
                print(f'Current balance: {self.balance}')


account = BankAccount(100)

threads = [
    threading.Thread(target=account.deposit,args=(10,)),
    threading.Thread(target=account.withdraw,args=(50,)),
    threading.Thread(target=account.deposit,args=(20,)),
    threading.Thread(target=account.get_balance),
    threading.Thread(target=account.withdraw,args=(30,))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()