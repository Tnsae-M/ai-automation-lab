# Week 3: Bots and Scheduling

## Project Overview

This project contains a simple Telegram weather bot built with Python. It can respond to Telegram commands and send a scheduled weather update.

## Features

- `/start` command to greet the user
- `/weather <city>` command to fetch the current weather for a city
- Scheduled weather updates for Addis Ababa

## Project Structure

- `telegram_weather_bot/main.py` - Starts the bot and runs the Telegram app
- `telegram_weather_bot/handler.py` - Handles bot commands
- `telegram_weather_bot/weather_service.py` - Fetches weather data from WeatherAPI
- `telegram_weather_bot/scheduler.py` - Sets up scheduled jobs
- `telegram_weather_bot/config.py` - Loads environment variables

## Setup

1. Navigate to the bot folder:
   ```bash
   cd telegram_weather_bot
   ```
2. Create a `.env` file in the same folder with the following values:
   ```env
   WEATHER_API_KEY=your_weatherapi_key
   TELEGRAM_API_KEY=your_telegram_bot_token
   CHAT_ID=your_chat_id
   ```
3. Install the required packages:
   ```bash
   pip install python-telegram-bot requests python-dotenv APScheduler
   ```
4. Run the bot:
   ```bash
   python main.py
   ```

## Usage

Once the bot is running:

- Send `/start` to see a welcome message
- Send `/weather Addis Ababa` to get the weather for a city

## Notes

- You need a valid WeatherAPI key to fetch weather data.
- The bot uses your Telegram bot token and chat ID for communication.
