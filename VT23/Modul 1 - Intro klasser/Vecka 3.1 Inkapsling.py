class Account:
    def __init__(self, id, password):
        self.id = id
        # 2 privata attribut
        self.__password = password
        self.__balance = 10000

    # Metoden deposit ändrar på objektens privata attribut balance
    def deposit(self):
        self.__printbalance()
        if (
            input("Skriv in ditt id") == self.id
            and input("Skriv in ditt lösenord") == self.__password
        ):
            cash = int(input("How much cash do you want to deposit?"))
            self.__balance += cash
        else:
            print("Wrong id or password")

    # Privat metod
    def __printbalance(self):
        print(self.__balance)


accounts = []
accounts.append(Account("1", "1234"))
accounts.append(Account("2", "123456"))
accounts.append(Account("Hampus", "5175"))
accounts[2].__printbalance()

accounts[2].deposit()
