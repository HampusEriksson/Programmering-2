#97-122
print(ord("j"))
print(chr(106+1))

ans = input("Skriv")
newans = ""

for c in ans:
    if c != " ":
        newans += chr(((ord(c)- 95) % 22)+96)
    else:
        newans += " "

print(newans)
