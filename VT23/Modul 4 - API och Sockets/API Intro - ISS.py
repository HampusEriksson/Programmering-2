import requests

response = requests.get("http://api.open-notify.org/astros.json")

if response.status_code == 200:
    print(response.text)
else:
    print("Kunde inte hämta fakta från API.")
