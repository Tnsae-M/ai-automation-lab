from apscheduler.schedulers.asyncio import AsyncIOScheduler
from weather_service import get_weather
from logger import setup_logger

logger=setup_logger()

def start_scheduler(application):
    scheduler = AsyncIOScheduler()

    async def weather_scheduled():
        weather=get_weather("Addis ababa")
        if not weather:
            logger.error("Something went wrong when fetching weather")
            return None
        chat_id=application.bot_data.get("chat_id")
        if not chat_id:
            logger.error("Chat ID not found in bot_data")
            return None
        city_name=weather["location"]["name"]
        country=weather["location"]["country"]
        temp_c=weather["current"]["temp_c"]
        condition=weather["current"]["condition"]["text"]
        message=(f"Weather fetched successfully. \ncity: {city_name}\\ncountry: {country}\ntemprature in Celcius: {temp_c}\ncondition: {condition} ")
        await application.bot.send_message(chat_id=application.chat_id, text=message)
        await application.bot.send.sens_message(chat_id=application.chat_id,text="Scheduler started successfully")
    scheduler.add_job(weather_scheduled,trigger='interval',seconds=10)
    scheduler.start()
    return scheduler
