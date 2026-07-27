from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://afriworket.com/jobs")
    page.wait_for_selector("a[href^='/jobs/']",timeout=30000)
    job_links=page.locator("a[href^='/jobs']")
    count=job_links.count()
    print(f"Found {count} job listings")
    for i in range(count):
        link=job_links.nth(i)
        title=link.inner_text()
        print("==========")
        print(link)
        print("==========")
        href=link.get_attribute("href")
        print(f"{title}->{href}")
    browser.close()