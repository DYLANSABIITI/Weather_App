from flask import Flask, render_template,jsonify,request
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv('.env')

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city")
        country = request.form.get('country')

        api_key = os.getenv("SECRET_KEY")



        url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial")
        data = url.json()
        '''
        return jsonify({
            'city': city,
            'country': country,
            'temp':data['main']['temp'],
            'humidity' : data['main']['humidity'],
            'wind_speed' : data['wind']['speed'],

        })
        '''
    

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']


        return render_template("index.html", city=city, temp=temp, humid=humidity, windspeed=wind_speed)


    else:
        return render_template("index.html")   

if __name__ == "__main__":
    app.run(debug=True)