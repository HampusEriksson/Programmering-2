class Account:

    def __init__(self, accountnr, password):
        self.__balance = 0.0
        self.transactions = []
        self.__accountnr = accountnr
        self.__password = password

    def __str__(self):
        return f"Accountnr: {self.__accountnr}\nBalance: {self.__balance}"

    def deposit(self, cash):
        if input("Account number:") == self.__accountnr and input("Password:") == self.__password:
            self.__balance += cash
        else:
            print("Invalid account number or password.")


accounts = []
accounts.append(Account("1", "Dante123"))
accounts.append(Account("2", "Noah123"))
accounts.append(Account("3", "Hampus123!"))

print(accounts[0])
