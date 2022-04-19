def typing_func():
    print("5" + 7)


while True:
    choice = input("1. Typing_func \n2. Quit\n")
    if choice == "1":
        typing_func()
    elif choice == "2":
        break


# Static - Detta program hade inte kunnat köra på grund av fel i compile time

# Dynamic - Detta program hade kunnat köra eftersom det blir fel under programmets gång när vi försöker addera en str med en integer


def double(i : int) -> int:
    return i * 2


mynumber = 5
print(double(mynumber))

