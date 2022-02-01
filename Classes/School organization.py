class Student:

    def __init__(self):
        """Varje elev ska ha dessa attribut:
        Personnummer, Namn, Ålder, Klass, Skola"""
        pass

    def __eq__(self, other):
        return self.personnr == other

    def change_school(self):
        pass


class School:

    def __init__(self):
        """Varje skola ska ha dessa attribut:
        Id, Namn, Adress, Elever """
        pass

    def add_student(self):
        pass

    def remove_student(self):
        pass


class Organization:

    def __init__(self):
        """Varje organisation ska ha dessa attribut:
        Id, Namn, Skolor"""
        pass

    def add_school(self):
        pass