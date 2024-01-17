class Grade:
    def __init__(self, grade, subject, points=100) -> None:
        self.grade = grade.capitalize()
        self.subject = subject.capitalize()
        self.points = points

    def __str__(self) -> str:
        return f"{self.grade} in {self.subject} worth {self.points}p."
