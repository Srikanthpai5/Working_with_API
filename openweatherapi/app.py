from flask import Flask, render_template, request, url_for
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city = request.form['city'].capitalize()
        country = request.form['country'].capitalize()
        api_key = "6954f831253553a7e68ac75de6785abf"

        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=metric')

        # print(weather_url.text) testing.
        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        min_temp = weather_data['main']['temp_min']
        max_temp = weather_data['main']['temp_max']

        # res = zip(city, country , str(temp), str(humidity), str(wind_speed), str(min_temp), str(max_temp) )
        # return render_template("result.html", msg=res)

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city, country=country, min_temp=min_temp, max_temp=max_temp)

    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)