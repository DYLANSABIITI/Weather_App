from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.args.get('city')
        country = request.args.get('country')

        api_key = "7b615df4505e553dd8ebb3a5e0b25be1"

        url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial")
        data = url.json()
        '''
        weather = {
            'city' : city,
            'temp' : data['main']['temp'],
            'humidity' : data['main']['humidity'],
            'wind_speed' : data['wind']['speed'],
            'description' : data['weather']['description'],
        }
        '''
        print(data)
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather']['description']


        return render_template("index.html", city=city, temp=temp, humid=humidity, windspeed=wind_speed, description=description)


    else:
        return render_template("index.html")    

if __name__ == "__main__":
    app.run(debug=True)