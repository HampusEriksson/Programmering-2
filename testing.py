while True:
    try:
        age = int(input("What is your age?"))

        if age > 50:
            print("Oh you are very much old.")
        else:
            print("Oh you are very much young.")
        break
    except ValueError:
        print("You did not enter an integer.")

print(age)