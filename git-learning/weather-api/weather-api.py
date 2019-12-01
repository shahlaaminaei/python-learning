import requests
import json

city = input("Please enter city name: ")
url = "https://samples.openweathermap.org/data/2.5/forecast?q="+city+"&appid=13eca1633098c789fce74164e10ef798"
response = requests.get(url)
j_pars = response.json()
print(j_pars['list'][2]['weather'][0]['description'])