import requests
import html
from config import telegram_key, chat_id

TG_API_URL = f"https://api.telegram.org/bot{telegram_key}/sendMessage"


def _post(payload: dict) -> None:
    response = requests.post(url=TG_API_URL, json=payload, timeout=15)
    response.raise_for_status()


def send_to_telegram(job_object, job_url: str = "") -> None:
    """Send a formatted HTML job alert to Telegram."""
    title = html.escape(job_object.title or "")
    company = html.escape(job_object.company or "Not specified")
    job_type = html.escape(job_object.job_type or "Not specified")
    experience_level = html.escape(job_object.experience_level or "Not specified")
    location = html.escape(job_object.location or "Not specified")
    summary = html.escape(job_object.summary or "")
    link = f'\n\n<a href="{job_url}">🔗 View Job →</a>' if job_url else ""

    text = (
        f"🆕 <b>{title}</b>\n\n"
        f"🏢 <b>Company:</b> {company}\n"
        f"📍 <b>Location:</b> {location}\n"
        f"💼 <b>Type:</b> {job_type}\n"
        f"📊 <b>Experience:</b> {experience_level}\n\n"
        f"📝 <b>Summary:</b>\n{summary}"
        f"{link}"
    )
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False,
    }
    try:
        _post(payload)
        print(f"Job sent to TG successfully: {title}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed sending job alert! error: {e}")


def send_alert(message: str) -> None:
    """Send a plain-text system alert (e.g. failure notification) to Telegram."""
    payload = {
        "chat_id": chat_id,
        "text": message,
    }
    try:
        _post(payload)
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed sending alert! error: {e}")