from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from weather_service import get_weather
from logger import setup_logger

logger=setup_logger()

def call_weather(city):
    weather=get_weather(city)
    if not weather:
        logger.error("Something went wrong when fetching weather")
        return None
    city_name=weather["location"]["name"]
    country=weather["location"]["country"]
    temp_c=weather["current"]["temp_c"]
    condition=weather["current"]["condition"]["text"]
    message=(f"Weather fetched successfully:\n" 
             f"city: {city_name}\n"
             f"country: {country}\n"
             f"temprature in Celcius: {temp_c}\n"
             f"condition: {condition} ")
    print(message)
logger.info("Starting" \
" the blocking scheduler...")

scheduler2=BlockingScheduler()
scheduler2.add_job(call_weather,CronTrigger(hour=11,minute=35),args=["Addis ababa"])
print(scheduler2.timezone)
scheduler2.start()
