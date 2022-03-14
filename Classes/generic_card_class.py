# Uppgift Generska klassser
# Fyll i de fyra tomma metoderna i klassen Card så att klassen kan jämföras med både int och str
# Kör sedan koden för att se om dina utskrifter matchar
# Det är inte säkert att det är 100% match beroende på hur du har implementerat klassen

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = []
for value in range(1, 14):
   for suit in suits:
       card = Card(value, suit)
       cards.append(card)

for c in cards:
   if c == 10:
       print(c)

"""Skriver ut(KAN SKRIVA UT ANNORLUNDA BASERAT PÅ DIN KLASS-IMPLEMENTATION!:
Clubs 10
Diamonds 10
Hearts 10
Spades 10"""

for c in cards:
   if c > 10 and c == "Diamonds":
       print(c)
"""
Jack of Diamonds
Queen of Diamonds 
King of Diamonds """


card = Card(5, "Diamonds")
for c in cards:
   if c == card:
       print(c)
"""
Diamonds 5
"""
for c in cards:
   if c == 5 and c > card:
       print(c)
"""
Hearts 5
Spades 5
"""
