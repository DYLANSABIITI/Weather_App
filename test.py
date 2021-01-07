import requests
import json
from dotenv import load_dotenv
import os
load_dotenv('.env')

city = "kampala"
country = "Uganda"
api_key = os.getenv("SECRET_KEY")

url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial")

data = url.json()

json_data = json.dumps(data, indent=2)

f = open("weather.json", "a")
f.write(str(json_data))
f.close
