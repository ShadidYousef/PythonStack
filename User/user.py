class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("client's name:",self.name,"balance:",self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance-=amount
        other_user.account_balance += amount
    

muath=User("Muath Alrefai", "rigahd@gmail.com")
kareem=User("Kareem Taha", "kareem@gmail.com")
yazan=User("Yazan Kayed", "yazan@gmail.com")
muath.make_deposit(500)
muath.make_deposit(100)
muath.make_deposit(150)
muath.make_withdrawal(100)
print("Muath's balance:", muath.account_balance)
kareem.make_deposit(300)
kareem.make_deposit(150)
kareem.make_withdrawal(50)
kareem.make_withdrawal(80)
print("Kareem's balance:", kareem.account_balance)
yazan.make_deposit(300)
yazan.make_withdrawal(50)
yazan.make_withdrawal(100)
yazan.make_withdrawal(50)
print("Yazan's balance:", yazan.account_balance)
muath.display_user_balance()
muath.transfer_money(yazan,50)
print("\t--after transfering balance:\n","\tyazan's balance:",yazan.account_balance,"\t muath's balance:", muath.account_balance)


