import sys
import json
import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

def _setup_logger():
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

def main():
	logger = _setup_logger()
	weather_api_key=os.environ.get("weather_api_key")
	city=input("enter name of city you want forcast from: ")
	params={
	"key":weather_api_key,
	"q":city,
	"aqi":"no"
	}
	url = f"http://api.weatherapi.com/v1/current.json"
	try:
		res = requests.get(url,params=params, timeout=10)
	except requests.exceptions.RequestException as e:
		# Log a concise single-line error; full traceback available at DEBUG level
		logger.error("Request failed for %s: %s", url,e)
		logger.debug("Request exception details", exc_info=True)
		sys.exit(2)

	status = res.status_code
	if status != 200:
		logger.error("HTTP %s for %s", status, url)
		text = res.text or "(no response body)"
		logger.debug(text[:1000])
		sys.exit(3)

	try:
		data = res.json()
	except ValueError as e:
		# Concise error message; retain response body at DEBUG level
		logger.error("Failed to decode JSON response: %s", e)
		logger.debug("Response body (truncated): %s", res.text[:1000])
		sys.exit(4)

	logger.info("Success (%s)", status)
	print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
	main()