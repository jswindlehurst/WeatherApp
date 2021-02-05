from flask import Flask, render_template
import requests
import os


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    query = "Calgary"
    unit = "metric"
    api_key = os.environ.get("API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units={2}".format(query, api_key, unit)
    data = requests.get(url=url)


    return render_template("index.html", data=data.json())

if __name__ == '__main__':
    app.run(debug=True)

