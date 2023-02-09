class Person:
    def __init__(self, name, age, socialnr):
        self.name = name
        self.age = age
        self.socialnr = socialnr


class Johan(Person):
    def __init__(self, age, socialnr):
        super(Johan, self).__init__("Johan", age, socialnr)
        self.long = True


class Fabian(Person):
    def __init__(self, age, socialnr):
        super(Fabian, self).__init__("Fabian", age, socialnr)
        self.cool = True


# Vi vill skapa klasser som vi kan använda flera gånger
# T.ex. då inte en klass som heter Johan som vi använder en gång
johan = Person("Johan", 17, "040838")
# johan = Johan(17, "040838")
fabian = Fabian(17, "041338")
