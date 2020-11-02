import requests
import json

city = "kampala"
country = "Uganda"
api_key = "7b615df4505e553dd8ebb3a5e0b25be1"

url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial")

data = url.json()

json_data = json.dumps(data, indent=2)

f = open("weather.json", "a")
f.write(str(json_data))
f.close


temp = round(data['main']['temp'])
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
description = data['weather']['description']
