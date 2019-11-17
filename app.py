import json

from flask import Flask

import weather

# print(" >>> ", sys.path)

app = Flask(__name__)

# Prima ruta care o ia din radacina din cauza la /

@app.route("/")
def hello():
    return "Hello, World!"

# A 2-a ruta care este verificate pe site doar cu /weather/ dupa ip

@app.route("/weather-cluj/")
def weather_route():
    temp = json.dumps(weather.weather())
    return temp

# A 3-a ruta

@app.route("/weather/my-cities/")
def weather_multiple_citites():
    return"Cluj:15, New York: 10"


