import requests

name = input("What's your name?")
response = requests.get('https://api.agify.io?name='+name)

answer = response.json()

print(f"Hello {name}. You are {answer['age']} years old. Your name has been inputted {answer['count']} times.")

