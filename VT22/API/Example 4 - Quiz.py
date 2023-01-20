#https://opentdb.com/api_config.php

import requests

amount = input("How many questions?")
diff = input("Which difficulty?")
response = requests.get(f"https://opentdb.com/api.php?amount={amount}&difficulty={diff}")
answer = response.json()

print(answer["results"][0]["question"])
input()
print(answer["results"][0]["correct_answer"])