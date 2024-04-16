import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
answer = response.json()

for x in answer:
    print(x)

for x in answer["bpi"]:
    print(x)

for x in answer["bpi"]["USD"]:
    print(x)


print(f"The price of 1 bitcoin in USD right now is {answer['bpi']['USD']['rate']}")
print(f"The price of 1 bitcoin in GBP right now is {answer['bpi']['GBP']['rate']}")
