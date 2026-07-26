from flask import Flask,render_template,redirect,request
import requests

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/details",methods=["POST"])
def details():
    city_name=request.form.get("city")
    api_key="5de2692ecc9acf75d671cc4f3f94fda9"
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response=requests.get(url)
    data=response.json()
    return render_template("details.html",data=data)

if __name__ == "__main__":
   app.run(debug=True)