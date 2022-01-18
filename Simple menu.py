# Simple menu with if
while True:
    choice = input("1. Create X\n2. Look at all X\n3. Quit\n").lower()
    print(choice in ["1", "create"])
    if choice in ["1", "create"]:
        #Create a new X
        pass

    elif choice in ["2" , "look"]:
        # Look at all X
        pass

    elif choice in ["3" , "quit"]:
        break

    else:
        print("Not a case")

# Simple menu with match case
while True:
    choice = input("1. Create X\n2. Look at all X\n3. Quit\n").lower()
    match choice:
        case "1" | "create":
            #Create a new X
            pass

        case "2" | "look":
            # Look at all X
            pass

        case "3" | "quit":
            break
        case _:
            print("Not a case")
