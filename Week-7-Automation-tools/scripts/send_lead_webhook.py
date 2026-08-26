import requests
import os
import time
import json
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
data_path=Path(__file__).parent/"test_payload.json"
webhook_url=os.getenv("WEBHOOK_URL")
with open(data_path,"r",encoding='utf-8') as f:
    data=json.load(f)
def send_lead_data():
    try:
        res=requests.post(webhook_url,json=data)
        res.raise_for_status()
        # make returns status code of 200 and accepted and it seems req.text is not catching it.
        return res.text
    except requests.exceptions.RequestException as e:
        print(f"something went wrong when sending the data!\nerror: {e}")

# For list of json lead objects
def send_leads_batch():
    if isinstance(data,list):
        for lead in data:
            try:
                res=requests.post(webhook_url,json=lead,timeout=10)
                res.raise_for_status()
                print(f"Sent {lead.get('name')}: {res.text}")
                time.sleep(1)
            except requests.exceptions.RequestException as e:
                print(f"something went wrong when sending the data!\nerror: {e}")
# send_lead_data()
send_leads_batch()