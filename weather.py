# import libraries
from argument_parser import args
# the config file contains the api key so it must not 
# be in the repository
try:
    from config import app_id, default_country_code
except ImportError as import_error:
    print("An error ocurred while trying to import the config file: ")
    print(import_error)

from forecast import Forecast

country_code = default_country_code
if args.country is not None:
    country_code = args.country

weather = Forecast(args.city, country_code, app_id)
weather.get_tomorrow()
