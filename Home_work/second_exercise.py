class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        return f"added {dep_amt} to the balance"

    def withdrawal(self,wd_amt):
        if self.balance >=wd_amt:
            self.balance = self.balance - wd_amt
            return "withdrawal accepted"
        return "sorry"

    def __str__(self):
        return f"owner: {self.owner}\nBalance: {self.balance}"

a = Account("nadav", 500)

print(a.owner)
print(a.balance)
print(a.deposit(50))
print(a.owner)
print(a.balance)
print(a.withdrawal(550))
print(a.owner)
print(a.balance)