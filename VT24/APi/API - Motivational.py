import requests, time, random


while True:
    if random.random() < 0.75:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        print(data[0]["q"])
    else:
        response = requests.get(
            "https://evilinsult.com/generate_insult.php?lang=en&type=json"
        )
        data = response.json()
        print(data["insult"])

    print("\n\n")
    time.sleep(5)
