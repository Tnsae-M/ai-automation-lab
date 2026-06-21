import sys
import json
import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

def setup_logger():
	# Simple, plain logging formatter (no color dependency)
	fmt = "%(asctime)s %(levelname)s: %(message)s"
	datefmt = "%Y-%m-%d %H:%M:%S"
	handler = logging.StreamHandler(stream=sys.stderr)
	handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

	logger = logging.getLogger("weather_app")
	logger.setLevel(logging.INFO)
	if not logger.handlers:
		logger.addHandler(handler)
	return logger

def get_weather(city_input,api_Key,logger):
	logger=setup_logger()
	params={
	"key":api_Key,
	"q":city_input,
	"aqi":"no"
	}
	url = f"https://api.weatherapi.com/v1/current.json"
	try:
		res=requests.get(url=url,params=params)
		res.raise_for_status()
		return res.json()
	except requests.exceptions.RequestException as e:
		logger.error("Requests failed: ",e)
		return None
def display_weather(data):
	location=data["location"]
	current=data["current"]
	print("Current weather forcast:")
	print(f"city: {location["name"]}")
	print(f"country: {location["country"]}")
	print(f"last updated: {current["last_updated"]}")
	print( f"temprature in celcius: {current["temp_c"]}")
	print(f"temprature in farenheit: {current["temp_f"]}")
	print(f"current condition: {current["condition"]["text"]}")

def main():
	logger=setup_logger()
	city=input("Enter city name: ").strip()
	if not city:
		logger.error("City name can't be empty")
		sys.exit(1)
	api=os.getenv("WEATHER_API_KEY")
	if not api:
		logger.error("Weather api key not found")
		sys.exit(1)
	weather_data=get_weather(city,api,logger)
	if weather_data:
		display_weather(weather_data)
if __name__ == "__main__":
	main()