# https://www.youtube.com/watch?v=jCzT9XFZ5bw&ab_channel=CoreySchafer
# @property
# Getter
# Setter


class NTIStudent:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # getter
    @property
    def email(self):
        return self.first + "." + self.last + "@elev.ga.ntig.se"

    @property
    def full_name(self):
        return self.first + " " + self.last

    # setter
    @full_name.setter
    def full_name(self, name):
        name = name.split(" ")
        self.first = name[0]
        self.last = name[1]

    # dåligt sätt
    def change_first(self, new_first):
        self.first = new_first
        self.email = self.first + "." + self.first + "@elev.ga.ntig.se"


students = []
students.append(NTIStudent("Fabian", "Barwich"))

students[0].full_name = "Ludwig Langeler"
print(students[0].first)
print(students[0].last)
print(students[0].email)

students[0].email = "Lukas"
