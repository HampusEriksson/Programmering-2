import requests

response = requests.get("http://api.open-notify.org/astros.json")

# .json konverterar response till dictionary
data = response.json()

if data["message"] == "success":
    print(f"There are currently {data['number']} people at ISS.")

    for person in data["people"]:
        print(person["name"])

else:
    print("Kunde inte hämta fakta från API.")
