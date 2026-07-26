from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://afriworket.com/jobs")
    page.wait_for_selector("a[href^='/jobs/']",timeout=15000)
    print("Job loaded")
    browser.close()