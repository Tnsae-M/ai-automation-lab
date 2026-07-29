from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
from pprint import pprint

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)

    try:
        page=browser.new_page()
        page.goto("https://afriworket.com/jobs")
        page.wait_for_selector("a[href^='/jobs/']",timeout=40000)
        job_links=page.locator("a[href^='/jobs/']")
        count=job_links.count()
        href_set=set()
        jobs=[]
        
        for i in range(count):
            link=job_links.nth(i)
            title=link.inner_text().strip()
            href=link.get_attribute("href")

            if not href or not title: 
                continue
            if href in href_set:
                continue
            href_set.add(href)
            jobs.append({
                    "Job":title,
                    "url":urljoin(page.url,href)
                })
        print(f"Found {len(jobs)} jobs!")
        pprint(jobs)
    finally:
        browser.close()