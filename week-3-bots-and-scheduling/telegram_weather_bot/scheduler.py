from apscheduler.schedulers.asyncio import AsyncIOScheduler
from weather_service import get_weather
from logger import setup_logger
import asyncio
logger=setup_logger()

def start_scheduler(application,chat_id):
    loop=asyncio.get_event_loop()
    scheduler = AsyncIOScheduler(event_loop=loop)

    async def weather_scheduled():
        weather=get_weather("Addis ababa")
        if not weather:
            logger.error("Something went wrong when fetching weather")
            return None
        # chat_id=application.bot_data.get("chat_id")
        # if not chat_id:
        #     logger.error("Chat ID not found in bot_data")
        #     return None
        city_name=weather["location"]["name"]
        country=weather["location"]["country"]
        temp_c=weather["current"]["temp_c"]
        condition=weather["current"]["condition"]["text"]
        message=(f"Weather fetched successfully:\n" 
                 f"city: {city_name}\n"
                 f"country: {country}\n"
                 f"temperature in Celsius: {temp_c}\n"
                 f"condition: {condition} ")
        await application.bot.send_message(chat_id=chat_id, text=message)
    # scheduler.add_job(weather_scheduled,trigger='interval',seconds=30)
    scheduler.add_job(weather_scheduled,trigger='cron',hour=22,minute=20)
    print("Scheduler started...")
    return scheduler
