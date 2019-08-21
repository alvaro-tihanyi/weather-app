import django
from flask import Flask, request
from django.template import Context
from django.conf import settings
from django.template.loader import get_template

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['views/'],
    }
]

app = Flask(__name__)

settings.configure(TEMPLATES=TEMPLATES)
django.setup()

@app.route('/', methods=["GET", "POST"])
def weather_app():
    context = {}
    if request.method == "POST" and request.form['city'] != '':
        from forecast import Forecast
        try:
            from config import app_id, default_country_code, icons
            weather = Forecast(request.form['city'], default_country_code, app_id)
            context['forecast'] = weather.get_tomorrow()
        except ImportError as import_error:
            context['forecast'] = {'error': "An error ocurred while loading the configuration file: " +  str(import_error)}

        if 'error' in context['forecast']:
            context['forecast']['icon'] = 'exclamation-triangle'
        else:
            # Since the api uses an 'atmosphere' category that groups various
            # phenomena, we use smog to represent them, as does the official
            # website of the api (OpenWeatherMap)
            context['forecast']['icon'] = 'smog'
            if context['forecast']['weather'] in icons:
                context['forecast']['icon'] = icons[context['forecast']['weather']]

    index = get_template("index.html")

    return index.render(context)