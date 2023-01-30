class Pet:
    def __init__(self, int, breed, loyalty, name, smell) -> None:
        self.int = int
        self.breed = breed
        self.loyalty = loyalty
        self.name = name
        self.smell = smell

    def __str__(self) -> str:
        return f""

    def get_smarter(self):
        self.int += 10


# class ClassName(SuperClass):
class Dog(Pet):
    def __init__(self, int, breed, loyalty, name) -> None:
        # Super refererar till klassen som vi ärver ifrån
        super(Dog, self).__init__(int, breed, loyalty, name, 100)
        self.commands = []

    def add_command(self):
        new_command = input("What command do you want to add?")
        self.commands.append(new_command)


class Cat(Pet):
    def __init__(self, int, breed, loyalty, name, smell, aggressive) -> None:
        # Super refererar till klassen som vi ärver ifrån
        super(Cat, self).__init__(int, breed, loyalty, name, smell)
        self.aggressive = aggressive

    def __str__(self) -> str:
        pass

    def empty_litter_box(self):
        print(f"The litter box is now empty, {self.name} can poop again.")


fido = Dog(0, "Husky", 100, "Fido")
print(fido.name)
fido.get_smarter()
castro = Cat(0, "Persian", -5, "Castro", 15, 205)

castro.empty_litter_box()


class Rabbit:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
