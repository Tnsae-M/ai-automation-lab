from playwright.sync_api import sync_playwright
from enricher import extract_emails,link_extractor,extract_about
url="https://gemini.google.com/"
with sync_playwright() as p:
    try:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()

        page.goto(url,wait_until='domcontentloaded',timeout=30000)
        # emails=extract_emails(page)
        # print(f"Found emails on {url}: ",emails)
        socials=extract_about(page=page)
        print(f"About extracted: {socials}")
        browser.close()
    except Exception as e:
        print(f"sth went wrong!\nError: {e}")
