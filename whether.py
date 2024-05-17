import requests
import json
city = input("Enter the name of the city\n")

url = "https://api.weatherapi.com/v1/current.json?key=d459bfd242034b5ab6175757240505&q={city}"

r = requests.get(url)
# print(r.text)
wdic =json.loads(r.text)
# print(wdic) 
print(wdic["current"]["temp_c"])

 