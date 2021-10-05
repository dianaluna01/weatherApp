import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weatherDashboard():
    return render_template('weather.html') 

@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']

    api_key = "39f0437c8f2e650838b190dba4c78ac7"
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('results.html', location=location, temp=temp, feels_like=feels_like, weather=weather)

def get_weather_results(zip_code, api_key):
    #removed {country code} because if not specified, it only defaults to USA codes
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    
    #will request data and return it in JSON format
    r = requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run(debug=True)
