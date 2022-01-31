class Elev:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other



elever = [Elev("Lukas"), Elev("Godson")]
print(elever.index("Lukas"))
