class Student:

    def __init__(self):
        """Varje elev ska ha dessa attribut:
        Personnummer, Namn, Ålder, Klass, Skola
        Datatyper: String, String, Int, String, School"""
        pass

    def __eq__(self, other):
        return self.personnr == other

    def change_school(self):
        pass

class School:

    def __init__(self):
        """Varje skola ska ha dessa attribut:
        Id, Namn, Adress, Elever
        Datatyper: String, String, String, [Student]"""
        pass

    def add_student(self):
        """Lägg till en elev"""
        pass

    def remove_student(self):
        """Ta bort en specifik elev"""
        pass

    def remove_class(self):
        """Ta bort alla elever från en specifik klass"""
        pass

    def change_address(self):
        pass


class Organization:

    def __init__(self):
        """Varje organisation ska ha dessa attribut:
        Id, Namn, Skolor
        Datatyper: String, String, [School]"""
        pass

    def add_school(self):
        pass