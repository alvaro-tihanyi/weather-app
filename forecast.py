import requests
import json
import datetime

class Forecast:
    def __init__(self, city, country, app_id):
        self.city = city
        self.country = country
        self.app_id = app_id

    # we use this method to get the element of a list with more occurrences
    # for example to get the majoritary kind of weather in a day
    def most_frequent(self, List): 
        counter = 0
        num = List[0] 
        
        for i in List: 
            curr_frequency = List.count(i) 
            if curr_frequency> counter: 
                counter = curr_frequency 
                num = i 
    
        return num 

    def get_tomorrow(self):
        forecast = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast?cnt=16&units=metric&q=" + self.city  + "," + self.country + "&appid=" + self.app_id)
            # since the api gives us an item for every 3 hours
            # given that we can only receive a maximum of 8 items per day we specify a count of 16 
            # to remove several days that we don't need
        forecast_json = forecast.json()

        if forecast_json['cod'] != '200':
            print("An error ocurred: (" + forecast_json['cod'] + ") " + forecast_json['message'].capitalize() + ".")
        else:
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            weather_list = []
            temperature_list = []

            # we store only the items that belong to tomorrow
            for item in forecast_json["list"]:
                if datetime.date.fromisoformat(item["dt_txt"].split(" ")[0]) == tomorrow:
                    weather_list.append(item["weather"][0]["main"]) # in the response, weather is a list (although it only has a single element in most cases)
                    temperature_list.append(item["main"]["temp"])
            
            # we get the most frequent weather type and the average temperature for tomorrow
            weather = self.most_frequent(weather_list)
            temperature = sum(temperature_list) / len(temperature_list)

            print("Weather forecast for tomorrow in " + 
                self.city + " (" + self.country + "): " + 
                    weather + ", Temperature " + (str(round(temperature)) + " ºC")
            )