from playwright.sync_api import sync_playwright
from email_extractor import extract_emails
url="https://www.galanicafe.com/"
with sync_playwright() as p:
    try:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()

        page.goto(url,wait_until='domcontentloaded',timeout=30000)
        emails=extract_emails(page)
        print(f"Found emails on {url}: ",emails)
        browser.close()
    except Exception as e:
        print(f"sth went wrong!\nError: {e}")
