from weather_service import get_weather
from telegram import Update
from telegram.ext import ContextTypes
from logger import setup_logger

logger = setup_logger()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to my weather forecast bot.")
    chat_id = update.effective_chat.id
    context.application.bot_data["chat_id"] = chat_id


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = " ".join(context.args)
    if not city:
        await update.message.reply_text("City not provided. please provide a city.")
        print("Missing city name!")
        return None

    weather = get_weather(city)
    if not weather:
        await update.message.reply_text("Something went wrong when fetching weather")
        logger.error("Something went wrong when fetching weather")
        return None

    city_name = weather["location"]["name"]
    country = weather["location"]["country"]
    temp_c = weather["current"]["temp_c"]
    condition = weather["current"]["condition"]["text"]
    await update.message.reply_text(
        f"Weather fetched successfully. \ncity: {city_name}\ncountry: {country}\ntemprature in Celcius: {temp_c}\ncondition: {condition} "
    )