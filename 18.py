class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            return "can't deposite 0 or less man"
    
    def withdraw(self, amount):
        if (amount <= self.__balance) and (amount>0):
            self.__balance -= amount
            return f"Withdrawal {amount}. New balance: {self.__balance}"
        else:
            return "insufficent balance please recharge ur account"
    

account = BankAccount("abeni",195)
print(account.deposit(5000))
print(account.withdraw(1500))
