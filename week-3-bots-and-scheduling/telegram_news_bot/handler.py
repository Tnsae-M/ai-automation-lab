import sys
import os
import requests
from dotenv import load_dotenv
from weather_service import get_weather
load_dotenv()
# needs city from tg bot
data=get_weather()
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
