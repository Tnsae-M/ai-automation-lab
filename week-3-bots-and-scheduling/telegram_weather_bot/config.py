from dotenv import load_dotenv
load_dotenv()
import os
from logger import setup_logger

def config():
    try:
        logger=setup_logger()
        weather_api=os.getenv("WEATHER_API_KEY")
        if not weather_api:
            logger.error("Weather api is missing")
        bot_api=os.getenv("TELEGRAM_API_KEY")
        if not bot_api:
            logger.error("Tg bot api key is missing")
        return {
            "weather_api":weather_api,
            "bot__api":bot_api
        }
    except Exception as e:
        logger.error("Connecting to Api failed: %s",e)