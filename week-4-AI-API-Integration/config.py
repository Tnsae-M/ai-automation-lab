import os
import sys
from dotenv import load_dotenv
load_dotenv()

openai_key=os.getenv("OPENAI_API_KEY")
if not openai_key:
    print("Something went wrong when fetching openai api key!")
    sys.exit(1)