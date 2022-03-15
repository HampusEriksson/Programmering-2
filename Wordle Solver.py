all_words = []
with open("wordlewords.txt", "r") as file:
    for line in file:
        all_words.append(line.strip("\n"))

while True:

    green = input("Input green")
    yellow = input("Input yellow")
    grey = input("Input grey")

    for i, word in enumerate(all_words):

        if any(a in grey for a in word):
            continue

        if not all(b in word for b in yellow):
            continue

        for j,c in enumerate(green):
            #print(j,c,word, green, len(green))
            #print(c != " " and word[j] != c)
            if c != " " and word[j] != c:
                break
        else:
            print(word)