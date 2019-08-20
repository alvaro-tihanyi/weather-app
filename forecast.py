import requests
import json

class Forecast:
    def __init__(self, city, country, app_id):
        self.city = city
        self.country = country
        self.app_id = app_id

    def get_tomorrow(self):
        forecast = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast?units=metric&q=" + self.city  + "," + self.country + "&appid=" + self.app_id)
        forecast_json = forecast.json()

        if forecast_json['cod'] != '200':
            print("An error ocurred: (" + forecast_json['cod'] + ") " + forecast_json['message'].capitalize() + ".")
        else:
            tomorrow_forecast = forecast_json["list"][0] # we only want tomorrow's forecast so we retrive only the first element of the list
            weather = tomorrow_forecast["weather"][0] # in the response, weather is a list (although it only has a single element in most cases)
            main = tomorrow_forecast['main']

            print("Weather forecast for tomorrow in " + 
                self.city + " (" + self.country + "): " + 
                    weather["main"] + ", Temperature " + str(main["temp"])
            )
