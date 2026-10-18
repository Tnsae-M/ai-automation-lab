# Production Readiness Audit — Job-alert-app-afriwork

> Cron schedule: `0 5 * * *` (runs once daily at 05:00 UTC via Railway)

**Verdict: ⚠️ Not production-ready yet.** It works, but it has critical gaps that will cause silent failures, spam, and maintenance pain.

---

## 🔴 Critical Issues (will silently break in production)

### 1. No Deduplication — Sends the Same Jobs Every Day
**File:** `main.py`

Every time the cron fires, it scrapes the full jobs page and sends **every listed job** to Telegram — including ones already sent yesterday. Users will get spammed with the same jobs repeatedly.

**Fix:** Persist a set of seen job URLs (e.g., in a Railway-attached PostgreSQL DB, a Redis set, or even a simple JSON file on a persistent volume). Only send jobs whose URLs haven't been seen before.

```python
# Example guard in main.py
if job["url"] not in seen_urls:
    send_to_telegram(job_summary)
    seen_urls.add(job["url"])
```

---

### 2. `browser.close()` Is Never Called — Resource Leak
**File:** `main.py`

The Playwright browser is launched but never explicitly closed. If the script crashes mid-run, the Chromium process leaks. On Railway's limited container resources this can cause OOM kills over time.

**Fix:** Use a `finally` block or the `with` context manager properly:

```python
try:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    # ... work ...
finally:
    browser.close()
```

---

### 3. Pinned Dependency Versions Are Missing
**File:** `requirements.txt`

```
playwright       # ← no version
google-genai     # ← no version
requests         # ← no version
python-dotenv    # ← no version
```

Unpinned deps mean a Railway rebuild next month could pull a **breaking version** and silently start failing. This is a critical production risk.

**Fix:**
```
playwright==1.49.0
google-genai==1.12.0
requests==2.32.3
python-dotenv==1.0.1
pydantic==2.10.6
```
(Run `pip freeze > requirements.txt` in your venv to get the exact versions you're already using.)

---

### 4. Wrong Gemini Model Name
**File:** `AI_summarizer.py` line 25

```python
model="gemini-3.1-flash-lite",   # ← This model does not exist
```

The current valid models are `gemini-2.0-flash`, `gemini-1.5-flash`, `gemini-1.5-pro`, etc. This is likely a typo that is either erroring silently or defaulting to something else.

**Fix:** Use a real model identifier, e.g.:
```python
model="gemini-2.0-flash-lite",
```

---

## 🟠 Major Gaps (will cause pain at scale)

### 5. No Telegram Message Formatting (Plain Text Only)
**File:** `send_to_telegram.py`

The message is sent as a raw flat string with no formatting. Telegram supports **MarkdownV2** and **HTML** — the current messages look ugly and are hard to scan on a phone.

**Fix:** Use `parse_mode=HTML` and structure the message:
```python
"text": f"<b>{title}</b>\n🏢 {company}\n📍 {location}\n⏱ {job_type}\n📊 {experience_level}\n\n{summary}\n\n<a href='{url}'>View Job →</a>",
"parse_mode": "HTML"
```

---

### 6. No Notification on Failure
**File:** `main.py`

If the whole run fails (Afriwork is down, scraper breaks, all jobs fail), you get **nothing** — no alert, no email, no Telegram message. You won't know the bot is broken until you manually check Railway logs.

**Fix:** Add a failure notification in the outer `except` block:
```python
except Exception as e:
    send_raw_telegram(f"🚨 Job alert bot FAILED: {e}")
```

---

### 7. Scraper Has No Rate Limiting / Politeness Delay
**File:** `scraper.py`

The scraper hits every job detail URL in a tight loop with no delay. This risks:
- Getting IP-banned by Afriwork
- Triggering bot detection (the site already requires `wait_for_load_state("networkidle")`)

**Fix:** Add a small delay between job detail requests:
```python
import time
time.sleep(1.5)  # between each job detail fetch
```

---

### 8. `pydantic` Is Not in `requirements.txt`
**File:** `requirements.txt`, `job_data_model.py`

`job_data_model.py` uses `pydantic` but it's not listed as a dependency. It works now only because `google-genai` happens to install it as a transitive dep — but that's not guaranteed.

**Fix:** Add `pydantic` explicitly to `requirements.txt`.

---

## 🟡 Minor Issues (code quality / maintainability)

### 9. Typo in AI Prompt
**File:** `AI_summarizer.py` line 26

```python
contents=f"Summerize this job: {job}",  # ← "Summerize" → "Summarize"
```

---

### 10. No `railway.toml` for Config-as-Code
The cron schedule (`0 5 * * *`) only exists in Railway's UI. If you redeploy to a new project or a teammate clones the repo, the schedule is lost.

**Fix:** Add a `railway.toml` at the project root:
```toml
[deploy]
cronSchedule = "0 5 * * *"
```

---

## ✅ What's Already Good

| Area | Status |
|---|---|
| Gemini retry logic (5 attempts, backoff) | ✅ Solid |
| Structured AI output via Pydantic schema | ✅ Good design |
| Per-job error isolation (one bad job doesn't kill the run) | ✅ Good |
| Headless Chromium via Playwright | ✅ Correct |
| Secrets via env vars (not hardcoded) | ✅ Good |
| Docker-based deployment | ✅ Correct approach |

---

## Priority Fix Order

| Priority | Issue |
|---|---|
| 🔴 1 | Fix model name (`gemini-3.1-flash-lite` → valid model) |
| 🔴 2 | Add deduplication (persistent seen-URLs store) |
| 🔴 3 | Pin dependency versions in `requirements.txt` + add `pydantic` |
| 🔴 4 | Close browser in `finally` block |
| 🟠 5 | Add failure alert Telegram notification |
| 🟠 6 | Add HTML formatting to Telegram messages + job URL |
| 🟠 7 | Add polite delay between scrape requests |
| 🟡 8 | Add `railway.toml` for cron config-as-code |
| 🟡 9 | Fix typo in AI prompt |
