import requests

# Example 1
budget = int(input("What is your budget?"))
while True:
    response = requests.get('https://www.boredapi.com/api/activity')
    response = response.json()
    if response["price"] <= budget:
        break

print(response["activity"])

# example 2
activities = []

for _ in range(10):
    response = requests.get('https://www.boredapi.com/api/activity')
    activities.append(response.json())

budget = int(input("What is your budget?"))

for a in activities:
    if a["price"] <= budget:
        print(a["activity"])
