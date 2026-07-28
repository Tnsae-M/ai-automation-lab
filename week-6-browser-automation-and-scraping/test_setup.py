from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://afriworket.com/jobs")
    page.wait_for_selector("a[href^='/jobs/']",timeout=30000)
    job_links=page.locator("a[href^='/jobs']")
    count=job_links.count()
    print(f"Found {count} job listings")
    href_set=set()
    for i in range(count):
        link=job_links.nth(i)
        title=link.inner_text()
        href=link.get_attribute("href")
        if href=="/jobs": 
            continue
        if not href in href_set:
            href_set.add(href)
            print(f"Job {i} link")
            print("===================")
            print(f"{title}->{href}")
            print("===================")
    browser.close()