# Du kan behöva köra "pip install requests" i terminalen, precis som i modul 3 för ursina.
import requests

# Mer info om denna API finns på https://restcountries.com/

response = requests.get("https://restcountries.com/v3.1/all?fields=name")
data = response.json()

if response.status_code == 200:
    for x in data:
        print(x["name"]["common"])


else:
    print("Kunde inte hämta länderna.")
