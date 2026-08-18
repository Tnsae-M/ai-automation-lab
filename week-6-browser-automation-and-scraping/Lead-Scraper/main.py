from osm_request_script import osm_request
from response_parser import parse_element
import os
import json
lead_folder_path=os.path.join("C:\\","_web_dev_files","CSEC-DEV","ai-automation-lab","week-6-browser-automation-and-scraping","Lead-Scraper","leads")
data_list=[]
city=input("Enter City: ")
res= osm_request(city)
for element in res["elements"]:
    try:
        item=parse_element(element)
        data_list.append(item)
    except Exception as e:
        print(f"Error occured! Error: {e}")
# print(data_list)
path_folder=os.path.join(lead_folder_path,f"{city}.json")
os.makedirs(lead_folder_path,exist_ok=True)
dicts_list=[ item.model_dump() for item in data_list]
with open(path_folder,"w") as file:
    json.dump(dicts_list,file,indent=2)
print(f"Lead data of {city} saved inside leads directory.")