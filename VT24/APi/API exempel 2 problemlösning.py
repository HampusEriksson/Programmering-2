import requests

response = requests.get("https://api.pokemontcg.io/v2/cards?q=name:psyduck")
answer = response.json()
"""
for key in answer.keys():
    print(key)
    print(answer[key])
    input()
"""


for item in answer["data"]:
    print(
        f'Name: {item["name"]}\nSet: {item["set"]["name"]}\nRarity: {item["rarity"] if item["rarity"] else "-"}'
    )

    input()
