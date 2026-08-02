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
        first_job_url=jobs[0]["url"]

        detail_page.goto(first_job_url,
                 wait_until="domcontentloaded",
                 timeout=40000)
        detail_page.wait_for_load_state("networkidle")

                # test for html structure.
        job_card = detail_page.locator("div.w-full.rounded-2xl.border.px-4.py-5")
        #contains job type,deadline, and sex
        job_type_container=job_card.locator("div.flex.flex-col.gap-2")
        #contains location and posted date
        location_container=job_card.locator("div.mt-2.flex.text-base.font-normal.text-gray-500.gap-3")
        #contains salary type and experience level
        salary_exp_container=job_card.locator("div.grid.gap-8.grid-cols-2")
        #contains job description
        job_description_container=job_card.locator("p.prose-xl.hyphens-auto.break-words.text-base.text-black")

        job_detail={
            "title":job_card.locator("h1").first.inner_text().strip(),
            "job_type":job_type_container.locator("p").nth(0).inner_text().strip().removeprefix("Job Type:").strip(),
            "location":location_container.locator("p").nth(1).inner_text().strip(),
            "salary_type":salary_exp_container.locator("p").nth(1).inner_text().strip(),
            "experience_level":salary_exp_container.locator("p").nth(2).inner_text().strip(),
            "description":job_description_container.locator("p").nth(0).inner_text().strip(),
            "url":first_job_url
        }
        print(job_detail)
    finally:
        browser.close()
