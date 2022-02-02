# Poly = Många Morph=Form → Polymorfism = många former

# Funktion med parameter som kallar på metod

class Computer:

    def run(self):
        print("Computer runs")


class Sprinter:

    def run(self):
        print("Sprinter runs")

def make_run(stuff):
    stuff.run()

c = Computer()
s = Sprinter()
make_run(c)
# Tecknet + betyder olika saker för olika klasser/datatyper.
print(5+3)
print("5"+"3")
print(["Vigor", "Jubin"] + ["Vigor", "Jubin"])
# Funktionen len() fungerar olika för olika datatyper
print(len("Ludwig"))
print(len(['Vigor', 'Jubin', 'Vigor', 'Jubin']))
# Polymorfism i klass-metoder
# Method overriding - Skriva om metoder från super-klasser

# Method overloading - Samma metod med flera olika parametrar
def summer(*args):
    print(args)
    s = 0
    for a in args:
        s += a
    return s

def summera(*args):
    if len(args)==2:
        pass
    if len(args)==3:
        pass


print(summera(5,3))