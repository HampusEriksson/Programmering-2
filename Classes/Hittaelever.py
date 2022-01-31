class Elev:

    def __init__(self, name, grade, personnr):
        self.name = name
        self.grade = grade
        self.personnr = personnr

    def __eq__(self, other):
        return self.personnr == other

    def raise_grade(self):
        self.grade += 1
        print(f"Grade raised to {self.grade}")

elever = [Elev("Ludwig", 15, "0401162478"), Elev("Daniel", 3, "0401162477"), Elev("Leon", 17, "0401162476"), Elev("Daniel", 5, "0401162473")]
hitta = input("Hitta elev: ")

if hitta in elever:
    print("Eleven finns")
    elever[elever.index(hitta)].raise_grade()

else:
    print("Eleven finns inte")