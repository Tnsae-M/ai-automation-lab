import os
import sys
from dotenv import load_dotenv
load_dotenv()

openai_key=os.getenv("OPENAI_API_KEY")
if not openai_key:
    print("Something went wrong when fetching openai api key!")
    sys.exit(1)
gemini_key=os.getenv("GEMINI_API_KEY")
if not gemini_key:
    print("No gemini key found in env")
    sys.exit(1)