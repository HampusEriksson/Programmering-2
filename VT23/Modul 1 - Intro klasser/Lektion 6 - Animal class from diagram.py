class Animal:
    def __init__(self, age, gender, mammal) -> None:
        self.age = age
        self.gender = gender
        self.mammal = mammal

    def isMammal(self):
        return self.mammal

    def mate(self):
        print("The animal mates.")


class Duck(Animal):
    def __init__(self, age, gender, beakcolor="Yellow") -> None:
        super(Duck, self).__init__(age, gender, False)
        self.beakcolor = beakcolor

    def swim(self):
        print("The duck swims")

    def quack(self):
        print("Quack quack")


class Fish(Animal):
    def __init__(self, age, gender, mammal, sizeInFt) -> None:
        super().__init__(age, gender, mammal)
        self.sizeInFt = sizeInFt
        # Alla fiskar kan ätas, wtf?
        self.canEat = True

    def swim(self):
        print("Swim swim...")


class Zebra(Animal):
    def __init__(self, age, gender, isWild=True) -> None:
        super(Zebra, self).__init__(age, gender, True)
        self.isWild = isWild

    def run(self):
        print("The zebra is running, vroom vroom..")


howard = Duck(2, "male")
howard.swim()
howard.quack()

isak = Fish(5, "male", False, 300)
isak.swim()

eddie = Zebra(17, "male")
eddie.run()

howard.mate()
isak.mate()
eddie.mate()
