from scraper import get_jobs,get_job_details
from playwright.sync_api import sync_playwright
from AI_summarizer import summarize_job
with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        jobs=get_jobs(page)
        for job in jobs:
            try:
                job_details=get_job_details(page,job["url"])
                job_summary=summarize_job(job_details)
                if job_summary is not None:
                    print(f"[{job_summary}]\n")
                else:
                    print("Job not summarized since returned None!\n")
            except Exception as e:
                    print(f"Error occured on job {job}\n error msg: {e}")
    except Exception as e:
        print(f"something went wrong! error message: {e}")
    
        