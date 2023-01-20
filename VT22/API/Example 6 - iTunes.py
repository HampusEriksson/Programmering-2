import requests

response = requests.get("https://itunes.apple.com/search?term=basshunter")

answer = response.json()

print("The names of all basshunter songs are:")

#TODO - Print out all basshunter songs from answer

#for key,value in answer.items():
#    print(key,":",value)

for song in answer["results"]:
    if song["artistName"] == "Basshunter":
        print(song["artistName"], ":",song["trackName"])
