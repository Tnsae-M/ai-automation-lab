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
        # pprint(jobs)

        detail_page=browser.new_page()
        first_job_url=jobs[1]["url"]

        detail_page.goto(first_job_url,
                 wait_until="domcontentloaded",
                 timeout=40000)
        detail_page.wait_for_load_state("networkidle")

                # test for html structure.
        paragraphs = detail_page.locator("p")
        job_title=detail_page.locator("h1").nth(0).inner_text()

        print(job_title)
        for i in range([4,3,10,9,12,11,13]):
            print(paragraphs.nth(i).inner_text())
        
    finally:
        browser.close()
