class Account:
    def __init__(self, id, password):
        """docstring"""
        self.id = id
        self.password = password
        self.balance = 10000

    def deposit(self, cash):
        if (
            input("Skriv in ditt id") == self.id
            and input("Skriv in ditt lösenord") == self.password
        ):
            self.balance += cash
        else:
            print("Wrong id or password")


accounts = []
accounts.append(Account("1", "1234"))
accounts.append(Account("2", "123456"))
accounts.append(Account("Hampus", "5175"))
