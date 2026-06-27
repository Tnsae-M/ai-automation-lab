from config import config
from telegram.ext import (ApplicationBuilder,CommandHandler)
from handler import start,weather


apis=config()
if apis is not None:
	bot_key=apis["bot_api"]
app=ApplicationBuilder().token(bot_key).build()
start_handler=CommandHandler("start",start)
app.add_handler(start_handler)
app.add_handler(CommandHandler("weather",weather))
print("Bot is listening...")

app.run_polling()
