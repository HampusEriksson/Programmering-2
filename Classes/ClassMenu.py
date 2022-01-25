class Pokemon:

    def __init__(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp

    def __str__(self):
        return self.name

all_pokemon = []
all_pokemon.append(Pokemon("Charizard", "Fire", 300))
all_pokemon.append(Pokemon("Pikachu", "Ligtning", 150))
all_pokemon.append(Pokemon("Blastoise", "Water", 250))

# Simple menu with if
while True:
    choice = input("1. Create Pokémon\n2. Look at all Pokémon\n3. Quit\n").lower()
    if choice in ["1", "create"]:
        all_pokemon.append(Pokemon(input("Name? "), input("Type? "), int(input("Hp? "))))


    elif choice in ["2" , "look"]:
       print(*all_pokemon)


    elif choice in ["3" , "quit"]:
        break

    else:
        print("Not a case")