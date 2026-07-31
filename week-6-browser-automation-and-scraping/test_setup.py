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
        job_card = detail_page.locator("div.w-full.rounded-2xl.border.px-4.py-5")
        paragraphs=job_card.locator("p")
        job_detail = {
            "title": job_card.locator("h1").first.inner_text().strip(),
            "location": paragraphs.nth(2).inner_text().strip(),
            "job_type": paragraphs.nth(3).inner_text().strip().removeprefix("Job Type:").strip(),
            "salary_type": paragraphs.nth(8).inner_text().strip(),
            "experience_level": paragraphs.nth(10).inner_text().strip(),
            "description": paragraphs.nth(12).inner_text().strip(),
            "url": first_job_url,
                    }
        print("===========")
        print(job_detail)
    finally:
        browser.close()
