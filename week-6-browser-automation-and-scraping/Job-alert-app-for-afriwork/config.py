import os
import sys
from dotenv import load_dotenv
load_dotenv()

gemini_key=os.getenv("GEMINI_API_KEY")
telegram_key=os.getenv("TELEGRAM_API_KEY")
chat_id=os.getenv("CHAT_ID")
if not gemini_key:
    print("Something went wrong when fetching gemini api key!")
    sys.exit(1)
if not telegram_key:
    print("Something went wrong when fetching telegram api key!")
    sys.exit(1)
if not chat_id:
    print("Something went wrong when fetching TG chat id!")
    sys.exit(1)