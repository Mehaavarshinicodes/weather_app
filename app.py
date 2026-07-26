from flask import Flask,render_template,redirect,request
import requests

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/details",methods=["POST"])
def details():
    #setting things for api call
    city_name=request.form.get("city")
    api_key="5de2692ecc9acf75d671cc4f3f94fda9"
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    #calling the api
    response=requests.get(url)

    #processing the data
    data=response.json()
    weather_description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    return render_template("details.html",
                           city_name=city_name,
                           weather_description=weather_description,
                           temp=temp,
                           feels_like=feels_like,
                           temp_min=temp_min,
                           temp_max=temp_max,
                           pressure=pressure,
                           humidity=humidity)

if __name__ == "__main__":
   app.run(debug=True)