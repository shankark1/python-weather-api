from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"

@app.route("/")
def home():
    return "Weather API App"

@app.route("/weather/<city>")
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "City not found"}

    data = response.json()

    result = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

    return jsonify(result)

app.run(debug=True)