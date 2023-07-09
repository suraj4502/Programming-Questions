class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.01):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def __init__(self, balance=0, monthly_fee=10):
        super().__init__(balance)
        self.monthly_fee = monthly_fee

    def deduct_monthly_fee(self):
        self.withdraw(self.monthly_fee)


class BusinessAccount(CheckingAccount):
    def __init__(self, balance=0, monthly_fee=10, overdraft_limit=1000):
        super().__init__(balance, monthly_fee)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Insufficient funds")
            return
        self.balance -= amount



my_account = BankAccount(100)
print(my_account.get_balance()) # 100

my_account.deposit(50)
print(my_account.get_balance()) # 150

my_account.withdraw(25)
print(my_account.get_balance()) # 125

my_account.withdraw(200) # Insufficient funds
print(my_account.get_balance()) # 125
