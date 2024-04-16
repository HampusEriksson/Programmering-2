import requests

response = requests.get("http://numbersapi.com/random/trivia")

if response.status_code == 200:
    print(response.text)
else:
    print("Kunde inte hämta fakta om talet.")
