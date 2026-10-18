from scraper import get_jobs, get_job_details
from playwright.sync_api import sync_playwright
from send_to_telegram import send_to_telegram, send_alert
from AI_summarizer import summarize_job
from seen_jobs import load_seen_urls, mark_as_seen

with sync_playwright() as p:
    browser = None
    try:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        seen_urls = load_seen_urls()
        jobs = get_jobs(page)
        sent_count = 0
        skipped_count = 0

        for job in jobs:
            job_url = job["url"]

            # --- Deduplication: skip jobs already sent ---
            if job_url in seen_urls:
                print(f"Skipping already-sent job: {job['Job']}")
                skipped_count += 1
                continue

            try:
                job_details = get_job_details(page, job_url)
                job_summary = summarize_job(job_details)
                if job_summary is not None:
                    send_to_telegram(job_summary, job_url)
                    mark_as_seen(job_url)
                    sent_count += 1
                else:
                    print(f"Job not summarized: {job['Job']}\n")
            except Exception as e:
                print(f"Error on job {job['Job']}: {e}")

        print(f"Run complete — sent: {sent_count}, skipped: {skipped_count}.")

    except Exception as e:
        error_msg = f"Job Alert Bot FAILED\n\nError: {e}"
        print(error_msg)
        send_alert(error_msg)

    finally:
        if browser:
            browser.close()
