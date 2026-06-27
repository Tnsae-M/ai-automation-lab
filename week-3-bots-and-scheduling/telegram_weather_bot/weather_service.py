import requests
from config import config
from logger import setup_logger
logger=setup_logger()
apis=config()
if apis is not None:
	api_key=apis["weather_api"]
def get_weather(city_input):
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
		logger.error("Requests failed: %s",e)
		return None