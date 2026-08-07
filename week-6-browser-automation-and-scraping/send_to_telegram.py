import requests
from config import telegram_key,chat_id
url=f'https://api.telegram.org/bot{telegram_key}/sendMessage'
def send_to_telegram(job_object):
    
  title=job_object.title
  company= job_object.company if job_object.company else "Not specified"
  job_type=job_object.job_type
  experience_level=job_object.experience_level
  location=job_object.location if job_object.location else "Not specified"
  summary=job_object.summary
  payload={
                "chat_id":chat_id,
                "text": f"title: {title}\ncompany: {company}\njob_type: {job_type}\nexperience_level: {experience_level}\nlocation: {location}\nsummary: {summary}"
            }
  try:
    response=requests.post(url=url,json=payload)
    response.raise_for_status()
    print(f"Job sent to TG successfully!")
  except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed! error: {e}")