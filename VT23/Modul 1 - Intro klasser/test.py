from dataclasses import dataclass


@dataclass
class BankAccount:
    balance: int = 0
    transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            self.transactions.append(("withdraw", amount))
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

    def generate_statement(self):
        for transaction in self.transactions:
            print(transaction[0], transaction[1])


b1 = BankAccount(1000)
b1.deposit(1000)
b1.generate_statement()
b2 = BankAccount(1000)
b2.deposit(2000)
b2.generate_statement()
