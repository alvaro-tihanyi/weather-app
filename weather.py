# import libraries
import sys
import requests
import json

# import own files
from argument_parser import args
# the config file contains the api key so it must not 
# be in the repository
from config import app_id, default_country_code

country_code = default_country_code
if args.country is not None:
    country_code = args.country

forecast = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast?units=metric&q=" + args.city  + "," + country_code + "&appid=" + app_id)
forecast_json = forecast.json()

if forecast_json['cod'] != '200':
    print("An error ocurred: (" + forecast_json['cod'] + ") " + forecast_json['message'].capitalize() + ".")
else:
    tomorrow_forecast = forecast_json["list"][0] # we only want tomorrow's forecast so we retrive only the first element of the list
    weather = tomorrow_forecast["weather"][0] # in the response, weather is a list (although it only has a single element in most cases)
    main = tomorrow_forecast['main']

    print("Weather forecast for tomorrow in " + 
        args.city + " (" + country_code + "): " + 
            weather["main"] + ", Temperature " + str(main["temp"])
    )
