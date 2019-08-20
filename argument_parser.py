# We use argparse to create a simple manual of the application
import argparse

parser = argparse.ArgumentParser(description="Get weather forecast for a city.")
parser.add_argument(
    "--country",
    help="""Country code in which to search the city.
    If it's not specified, the default country code in the config file will be used.
    Examples: Brazil = BR, United Kingdom = UK"""
)

# We specify that the city is required so argparse will validate
# the parameters for us.
required_args = parser.add_argument_group("Required named arguments")
required_args.add_argument(
    "--city", 
    help="City in which to check the weather.", 
    required=True
)

args = parser.parse_args()