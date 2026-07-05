from config import config
from telegram.ext import (ApplicationBuilder,CommandHandler)
from handler import start,weather
from scheduler import start_scheduler
apis=config()
if apis is not None:
	bot_key=apis["bot_api"]
	chat_id=apis["chat_id"]
app=ApplicationBuilder().token(bot_key).build()
start_handler=CommandHandler("start",start)
app.add_handler(start_handler)
app.add_handler(CommandHandler("weather",weather))
scheduler=start_scheduler(app,chat_id)
if __name__=="__main__":
	print("Bot is listening...")
	scheduler.start()
	try:
		app.run_polling()
	except KeyboardInterrupt:
		print("Shutting down...")