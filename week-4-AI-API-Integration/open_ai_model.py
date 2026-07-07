from openai import OpenAI
from config import openai_key
client = OpenAI(
  api_key=openai_key
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="which one has better future comparing going deep and going wide in software engineering?",
  store=True,
)
print(response.output_text);
