class BankAccount:
    def __init__(self, interest_rate=0.02, balance=0):
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
    
class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate = 0.02, balance=0)
    def display_user_balance(self):
        print("client's name:",self.name,"balance:",self.account.balance)
    def transfer_money(self, other_user, amount):
        self.account.balance-=amount
        other_user.account.balance += amount

muath = User("Muath", "rigahd@gmail.com")
muath.account.deposit(200).withdraw(50).yield_interest().display_account_info()
muath.display_user_balance()