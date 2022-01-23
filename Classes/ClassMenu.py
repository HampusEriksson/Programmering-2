class Pokemon:
    def __init__(self, name, type, hp):
        """Each Pokémon has a name, a type and hp"""
        self.name = name
        self.type = type
        self.hp = hp

    def __str__(self):
        """The str method returns the name of the Pokémon"""
        return self.name


all_pokemon = []
all_pokemon
# Simple menu with if
while True:
    choice = input("1. Create X\n2. Look at all X\n3. Quit\n").lower()
    if choice in ["1", "create"]:
        # Create a new X
        pass

    elif choice in ["2", "look"]:
        # Look at all X
        pass

    elif choice in ["3", "quit"]:
        break

    else:
        print("Not a case")
