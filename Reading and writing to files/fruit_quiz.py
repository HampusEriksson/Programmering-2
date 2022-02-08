import random


def file_to_dict(filepath):
    newdict = {}
    with open(filepath, "r", encoding="utf8") as file:
        for rad in file:
            rad = rad.strip("\n")
            rad = rad.split(",")
            newdict[rad[0]] = rad[1]
    return newdict



mydict = file_to_dict("Fruits.csv")
print(mydict)

while True:
    f = random.choice(list(mydict.keys()))
    svar = input(f"Vad betyder {f}?").lower()
    if svar == mydict[f]:
        print("Rätt")
    else:
        print("Fel")