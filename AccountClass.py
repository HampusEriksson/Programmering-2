class Account:
    
    def __init__(self, id, password):
        self.__id = id
        self.__password = password
        self.__balance = 10000
        
    def __deposit(self, cash):
        if input("Skriv in ditt id") == self.id and input("Skriv in ditt lösenord") == self.password:
            self.balance += cash
        else:
            print("Wrong id or password")

        
        
accounts = []
accounts.append(Account("1", "1234"))
accounts.append(Account("2", "123456"))
accounts.append(Account("Hampus", "5175"))
accounts[0].test()
