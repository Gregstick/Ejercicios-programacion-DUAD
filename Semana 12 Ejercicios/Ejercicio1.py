class BankAccount():
    def __init__(self):
        self.balance = 0

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance -= amount
    

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.balance = 0
        self.min_balance = min_balance

    def amount_to_withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("No puedes retirar, el saldo quedaría debajo del mínimo permitido.")
        else:
            self.balance -= amount
            print("Retiro exitoso")


bank_account = BankAccount()
bank_account.add_balance(200)
print("Balance actual: ", bank_account.balance)
bank_account.subtract_balance(50)
print("Balance actual: ", bank_account.balance)

savings = SavingsAccount(50)
savings.add_balance(200)
savings.amount_to_withdraw(120)
savings.amount_to_withdraw(60)