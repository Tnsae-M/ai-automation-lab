from scraper import get_jobs,get_job_details
from playwright.sync_api import sync_playwright
from AI_summarizer import summarize_job
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    try:
        jobs=get_jobs(page)
        for job in jobs:
            job_details=get_job_details(page,job["url"])
            job_summary=summarize_job(job_details)
            print(job_summary)
        browser.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        browser.close()