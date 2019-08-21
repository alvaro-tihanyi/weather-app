# Weather App

A Python application to check tomorrow's weather in a specific city.

## Requirements
* Python3.7
* An [OpenWeatherMap](https://openweathermap.org/) API Key
* Flask
* Django

## Installation
First of all, we clone the repository:

    git clone https://github.com/alvaro-tihanyi/weather-app.git
Note: Remember to have a Python3.7 environment to be able to install and use the application.

After that, we access the new directory and install the requirements:
  
    cd weather-app
    pip install -r requirements.txt


## Usage
We configurate flask. On linux we would do:

    FLASK_APP=app.py

In case we are in Windows, we would do the following:

    set FLASK_APP=app.py
    
Then we run Flask:

    flask run
    
We then access our local host (127.0.0.1):

![Empty index screen](https://raw.githubusercontent.com/alvaro-tihanyi/weather-app/flask_integration/documentation/images/doc_capture_1.PNG)

We can input a city and then get the weather for tomorrow:

![Empty index screen](https://raw.githubusercontent.com/alvaro-tihanyi/weather-app/flask_integration/documentation/images/doc_capture_2.PNG)