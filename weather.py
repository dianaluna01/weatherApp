import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weatherDashboard():
    return render_template('weather.html') 

@app.route('/results', methods=['POST'])
def displayInfo():
    zip_code = request.form['zipCode']

    api_key = "34a7ee6dda364f4215900946c63d9153"
    data = info(zip_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    place = data["name"]

    return render_template('results.html', place=place, temp=temp, feels_like=feels_like, weather=weather)

def info(zip_code, api_key):
    #removed {country code} because if not specified, it only defaults to USA codes
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    
    #will request data and return it in JSON format
    r = requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run()
