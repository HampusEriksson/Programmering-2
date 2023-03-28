import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
answer = response.json()

for key in answer:
    print(key)


for key in answer["bpi"]:
    print(key)

for key in answer["bpi"]["EUR"]:
    print(key)

""" Detta kraschar, svar hittat
for key in answer["bpi"]["EUR"]["rate_float"]:
    print(key)
"""

# TODO - Skriv korrekt läsning av bitcoin pris från answer
print(f'One bitcoin is worth {answer["bpi"]["EUR"]["rate_float"]} EUR right now.')
