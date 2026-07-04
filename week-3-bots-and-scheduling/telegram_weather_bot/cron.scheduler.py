import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from weather_service import get_weather
from logger import setup_logger

logger=setup_logger()
def listner(event):
    if event.exception:
        logger.error("The job crashed :(")
    else:
        logger.info("The job worked :)")
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
    logger.info(message)
logger.info("Starting" \
" the blocking scheduler...")

scheduler2=BlockingScheduler()
trigger=CronTrigger(hour=12,minute=32)
job=scheduler2.add_job(call_weather,trigger=trigger,args=["Addis ababa"])
scheduler2.add_listener(listner,EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
print(scheduler2.timezone)
logger.info(f"Next fire is scheduled at {trigger.get_next_fire_time(None,datetime.datetime.now(scheduler2.timezone))}")
scheduler2.start()