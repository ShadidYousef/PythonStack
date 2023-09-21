class BankAccount:
    def __init__(self, interest_rate=0.01, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("insufficient funds: Charing a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

account1 = BankAccount()
account2= BankAccount()
account1.deposit(500).deposit(200).deposit(300).withdraw(200).yield_interest().display_account_info()
account2.deposit(500).deposit(300).withdraw(200).withdraw(100).withdraw(150).withdraw(50).yield_interest().display_account_info()