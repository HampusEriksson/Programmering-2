import requests

par = input("How many people yes?")
response = requests.get("https://www.boredapi.com/api/activity?participants=" + par)

answer = response.json()

print(f"I think you should go and {answer['activity'].lower()}.")