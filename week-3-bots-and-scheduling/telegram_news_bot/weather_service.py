import sys
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

def get_weather(city_input):
	api_key=os.getenv("WEATHER_API_KEY")
	logger=setup_logger()
	if not api_key:
		logger.error("API key missing")
	params={
	"key":api_key,
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