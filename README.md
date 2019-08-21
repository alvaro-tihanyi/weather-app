# Weather App

A Python application to check tomorrow's weather in a specific city.

## Requirements
* Python3.7
* Flask
* Django

## Installation
First of all, we clone the repository:

    git clone https://github.com/alvaro-tihanyi/weather-app.git
**Note**: Remember to have a Python3.7 environment to be able to install and use the application.

After that, we access the new directory and install the requirements:
  
    cd weather-app
    pip install -r requirements.txt


## Usage
**Note**: By default, the application searchs for cities in Spain (country code ES), if we want to search cities in another country we need to specify it in the config.py file. For example:

```python
default_country_code = "UK"
```

In order to start the server we need to first configurate flask.
On linux we would do:

    FLASK_APP=app.py

In case we are in Windows, we would do the following:

    set FLASK_APP=app.py
    
Then we run Flask:

    flask run
    
We then access our local host (127.0.0.1):

![Empty index screen](https://raw.githubusercontent.com/alvaro-tihanyi/weather-app/flask_integration/documentation/images/doc_capture_1.PNG)

We can input a city and then get the weather for tomorrow:

![Index screen with weather information](https://raw.githubusercontent.com/alvaro-tihanyi/weather-app/flask_integration/documentation/images/doc_capture_2.PNG)

Finally, here is a list of cities to test de application:
* Barcelona
* Madrid
* Palma de Mallorca
* Bilbao
* Sevilla
* Zaragoza

## Time spent
Approximately 9 hours.