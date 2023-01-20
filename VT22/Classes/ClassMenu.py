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
all_pokemon.append(Pokemon("Charizard", "Fire", 300))
all_pokemon.append(Pokemon("Pikachu", "Ligtning", 150))
all_pokemon.append(Pokemon("Blastoise", "Water", 250))

# Simple menu with if
while True:
    choice = input("1. Create Pokémon\n2. Look at all Pokémon\n3. Quit\n").lower()
    if choice in ["1", "create"]:
<<<<<<< HEAD
        all_pokemon.append(Pokemon(input("Name? "), input("Type? "), int(input("Hp? "))))


    elif choice in ["2" , "look"]:
       print(*all_pokemon)

=======
        # Create a new X
        pass

    elif choice in ["2", "look"]:
        # Look at all X
        pass
>>>>>>> 7497861dcf9b1d574652b621b4e691119adaafa2

    elif choice in ["3", "quit"]:
        break

    else:
        print("Not a case")
