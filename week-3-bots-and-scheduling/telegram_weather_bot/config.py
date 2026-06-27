from dotenv import load_dotenv
load_dotenv()
import sys
import os
from logger import setup_logger

def config():
    try:
        logger=setup_logger()
        weather_api=os.getenv("WEATHER_API_KEY")
        if not weather_api:
            logger.error("Weather api is missing")
            sys.exit(1)
        bot_api=os.getenv("TELEGRAM_API_KEY")
        if not bot_api:
            logger.error("Tg bot api key is missing")
            sys.exit(1)
        return {
            "weather_api":weather_api,
            "bot_api":bot_api
        }
    except Exception as e:
        logger.error("Connecting to Api failed: %s",e)