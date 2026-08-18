import re
from urllib.parse import unquote
from playwright.sync_api import Page

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def _extract_mailto(page: Page) -> set[str]:
    found: set[str] = set()

    # Query all anchor tags where href contains 'mailto:'
    hrefs: list[str] = page.eval_on_selector_all(
        'a[href*="mailto:" i]',
        'elements => elements.map(el => el.getAttribute("href"))'
    )

    for href in hrefs:
        if not href or 'mailto:' not in href.lower():
            continue

        _, _, raw_target = href.partition('mailto:')
        clean_target = raw_target.split('?')[0].strip()
        decoded = unquote(clean_target).strip()

        for candidate in decoded.split(','):
            candidate = candidate.strip().lower()
            if EMAIL_REGEX.match(candidate):
                found.add(candidate)

    return found

def extract_emails(page: Page) -> set[str]:
    results: set[str] = set()
    results.update(_extract_mailto(page))
    return results