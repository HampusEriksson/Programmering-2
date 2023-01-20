import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

answer = response.json()

for key, value in answer["bpi"]["GBP"].items():
    print(key, " : ", value)

print(answer["bpi"]["GBP"]["rate_float"])
