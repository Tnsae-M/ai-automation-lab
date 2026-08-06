import os
import sys
from dotenv import load_dotenv
load_dotenv()

gemini_key=os.getenv("GEMINI_API_KEY")
if not gemini_key:
    print("Something went wrong when fetching gemini api key!")
    sys.exit(1)
