from osm_request_script import osm_request
from response_parser import parse_element
from enricher import enrich_data
from pathlib import Path
from playwright.sync_api import sync_playwright
import os
import json
# This is a V1 build for this lead scraper. and from what I noticed there is a queue issue on large datasets(i.e paris). this needs to be fixed for it to be really usable by me or others. run the script on paris and you will see why.
lead_folder_path=Path(__file__).parent/'leads'
data_list=[]
with sync_playwright() as p:
    city=input("Enter City: ")
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    try:
        res= osm_request(city)
        for element in res["elements"]:
            try:
                item=parse_element(element)
                enrich_data(item,page)
                data_list.append(item)
            except Exception as e:
                print(f"Error occured! Error: {e}")
        path_folder=os.path.join(lead_folder_path,f"{city}.json")
        os.makedirs(lead_folder_path,exist_ok=True)
        dicts_list=[ item.model_dump(mode='json') for item in data_list]
        with open(path_folder,"w") as file:
            json.dump(dicts_list,file,indent=2)
        print(f"Lead data of {city} saved inside leads directory.")
    except Exception as e:
        print(f"Something went wrong when wiring the whole system.\nerror: {e}")
        