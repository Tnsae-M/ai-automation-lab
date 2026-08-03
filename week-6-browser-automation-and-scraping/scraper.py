from playwright.sync_api import sync_playwright
from urllib.parse import urljoin

def get_jobs(page):
        try:
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
            return jobs
        except Exception as e:
            print(f"An error occurred while getting job links: {e}")


def get_job_details(page,job_url):
        try:
            page.goto(job_url,
                    wait_until="domcontentloaded",
                    timeout=40000)
            page.wait_for_load_state("networkidle")
            job_card = page.locator("div.w-full.rounded-2xl.border.px-4.py-5")
            job_type_container=job_card.locator("div.flex.flex-col.gap-2")
            location_container=job_card.locator("div.mt-2.flex.text-base.font-normal.text-gray-500.gap-3")
            salary_exp_container=job_card.locator("div.grid.gap-8.grid-cols-2")
            job_description_container=job_card.locator("p.prose-xl.hyphens-auto.break-words.text-base.text-black")

            job_detail={
                "title":job_card.locator("h1").first.inner_text().strip(),
                "job_type":job_type_container.locator("p").nth(0).inner_text().strip().removeprefix("Job Type:").strip(),
                "location":location_container.locator("p").nth(1).inner_text().strip(),
                "salary_type":salary_exp_container.locator("p").nth(0).inner_text().strip(),
                "experience_level":salary_exp_container.locator("p").nth(2).inner_text().strip(),
                "description":job_description_container.locator("p").nth(0).inner_text().strip(),
                "url":job_url
            }
            return job_detail
        except Exception as e:
            print(f"An error occurred while fetching job details: {e}")