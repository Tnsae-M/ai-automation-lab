from google import genai
from config import gemini_key
client = genai.Client(
    api_key=gemini_key
)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="you are a senior freelancer,Tell me how I can land an internation remote job that pays in dollars as an ethiopian backend developer using TS or JS as a language? consider that I have 2 years of experience in node.js developement and I have a portfolio of 5 projects that I can show to potential clients. Also, give me a list of 10 websites where I can find such jobs?"
)
print(interaction.output_text)