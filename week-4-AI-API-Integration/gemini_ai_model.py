from google import genai
from google.genai import types
from config import gemini_key
client = genai.Client(
    api_key=gemini_key
)
search_tool=types.Tool(google_search=types.GoogleSearch())
config=types.GenerateContentConfig(tools=[search_tool])
# interaction = client.interactions.create(
#     model="gemini-3.5-flash",
#     input="you are a senior freelancer,Tell me how I can land an internation remote job that pays in dollars as an ethiopian backend developer using TS or JS as a language? consider that I have 2 years of experience in node.js developement and I have a portfolio of 5 projects that I can show to potential clients. Also, give me a list of 10 websites where I can find such jobs?"
# )
#  print("Response 1: ",interaction.output_text)

# interaction_2= client.interactions.create(
#     model="gemini-3.5-flash",
#     input="from the previous answer, pick out the top 5 websites that I can focus on?",
#     previous_interaction_id=interaction.id
# )
#  print("Response 2: ",interaction_2.output_text)
# response=client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents="Give me a short report about mercor AI job finding platform? use the latest information in a range of 2-3 weeks before today as a source."
# )
#  print(response.text)
chat=client.chats.create(model="gemini-2.5-flash",config=config)

res1=chat.send_message("Give me a short report about mercor AI job finding platform? use the latest information in a range of 2-3 weeks before today as a source.")
# print(res1.text)
print("SPACE BETWEEN RESPONSES \n \n \n")
res2=chat.send_message("verify your sources as of today, july 8,2026")
# print(res2.text)
print("SPACE BETWEEN RESPONSES \n \n \n")
for res in [res1, res2]:
    meta = res.candidates[0].grounding_metadata
    if meta and meta.web_search_queries:
        print("Searched:", meta.web_search_queries)