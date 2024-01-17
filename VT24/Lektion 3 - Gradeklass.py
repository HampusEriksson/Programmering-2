from my_classes import Grade


my_grades = []
grade_points = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "F": 0}
while True:
    choice = input("1. Add grade\n2. Look at grades\n3. Print meritvalue\n4. Quit\n")

    if choice == "1":
        grade = input("\nGrade: ")
        subject = input("Subject: ")
        points = input("Points(leave blank if 100): ")
        if points in ["50", "100", "150"]:
            my_grades.append(Grade(grade, subject, int(points)))

        elif points == "":
            my_grades.append(Grade(grade, subject))

        else:
            print("Invalid points")
    elif choice == "2":
        for grade in my_grades:
            print(grade)

    elif choice == "3":
        total_points = 0
        merit = 0
        for grade in my_grades:
            total_points += grade.points
            merit += grade.points * grade_points[grade.grade]

        print(f"Merit value: {merit/total_points:.2f}")

    elif choice == "4":
        print("Good bye")
        break
