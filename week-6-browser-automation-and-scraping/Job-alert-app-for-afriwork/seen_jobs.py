import os
import requests

UPSTASH_URL = os.getenv("UPSTASH_REDIS_REST_URL", "").rstrip("/")
UPSTASH_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN", "")
SET_KEY = "seen_job_urls"

_ENABLED = bool(UPSTASH_URL and UPSTASH_TOKEN)


def _headers() -> dict:
    return {"Authorization": f"Bearer {UPSTASH_TOKEN}"}


def _run_command(command: list) -> dict | None:
    """Send a single Redis command to Upstash REST API."""
    try:
        res = requests.post(UPSTASH_URL, json=command, headers=_headers(), timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"Warning: Upstash Redis error: {e}")
        return None


def load_seen_urls() -> set[str]:
    """Return the set of job URLs already sent to Telegram."""
    if not _ENABLED:
        print("Warning: Upstash not configured — deduplication disabled.")
        return set()
    result = _run_command(["SMEMBERS", SET_KEY])
    if result and isinstance(result.get("result"), list):
        return set(result["result"])
    return set()


def mark_as_seen(url: str) -> None:
    """Add a job URL to the seen set so it won't be sent again."""
    if not _ENABLED:
        return
    _run_command(["SADD", SET_KEY, url])
