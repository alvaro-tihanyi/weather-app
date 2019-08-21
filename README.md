# Weather App

A Python application to check tomorrow's weather in a specific city.

## Requirements
* Python3.6
* An [OpenWeatherMap](https://openweathermap.org/) API Key

## Installation
First of all, we clone the repository:

    > git clone https://github.com/alvaro-tihanyi/weather-app.git
After that, we access the new directory and install the requirements:
  
    > cd weather-app
    > pip install -r requirements.txt


## Usage


    weather.py [-h] [--country COUNTRY] --city CITY
    
    Get weather forecast for a city.
    
    Optional arguments:
      -h, --help         show this help message and exit
      --country COUNTRY  Country code in which to search the city. If it's not
                         specified, the default country code in the config file
                         will be used. Examples: Brazil = BR, United Kingdom = UK
    
    Required named arguments:
      --city CITY        City in which to check the weather.

Therefore, if we wanted to get the weather for London we would do the following:

    > python weather.py --city=London --country=UK
    Weather forecast for tomorrow in London (UK): Clear, Temperature 19.36

Alternatively,  we can specify the default country code in the config file, like this:
```python
default_country_code =  "UK"
````
Then, we only need to specify the city:

    > python weather.py --city=Oxford
    Weather forecast for tomorrow in Oxford (UK): Clear, Temperature 18.35
In case the city is not found, the application will throw an error. For example, if we try to get the weather 
for Madrid while having "UK" as our default country code:

    > python weather.py --city="Madrid"
    An error ocurred: (404) City not found.

## Time spent
Approximately 4 hours.