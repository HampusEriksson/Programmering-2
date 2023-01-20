import requests

# Uppgift 4

response = requests.get("https://date.nager.at/api/v2/publicholidays/2020/US")
answer = response.json()
print('The big holidays in the US are:')

for x in answer:
    print(x['localName'])

# Uppgift 5

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=mojito")
answer = response.json()
print('The different mojito drinks I can offer is:')
for x in answer['drinks']:
    print(x['strDrink'])