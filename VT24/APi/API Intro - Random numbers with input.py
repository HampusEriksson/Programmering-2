import requests

number = input("Write a number that you want trivia about.")
response = requests.get(f"http://numbersapi.com/{number}")

if response.status_code == 200:
    print(response.text)
else:
    print("Kunde inte hämta fakta om talet.")
