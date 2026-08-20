import re
from urllib.parse import unquote
from playwright.sync_api import Page
import json
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',re.IGNORECASE)
EMAIL_STRICT_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)
IGNORED_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.css', '.js')

def _clean_and_validate(candidate:str)->str|None:
    clean_cand=candidate.strip().strip('.,;:()[]{}<>\"\'').lower()
    if any(clean_cand.endswith(ext) for ext in IGNORED_EXTENSIONS):
        return None
    if EMAIL_STRICT_REGEX.match(clean_cand):
        return clean_cand
    return None

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
            valid_cand=_clean_and_validate(candidate)
            if valid_cand:
                found.add(valid_cand)

    return found
def _extract_json_ld(page:Page)->set[str]:
    found:set[str]=set()
    raw_scripts:list[str]=page.eval_on_selector_all(
        'script[type="application/ld+json"]',
        'elements => elements.map(el => el.textContent)')
    for script in raw_scripts:
        if not script:
            continue
        try:
            parsed=json.loads(script)
            serialized=json.dumps(parsed)
            for match in EMAIL_REGEX.findall(serialized):
                valid=_clean_and_validate(match)
                if valid:
                    found.add(valid)
        except (json.JSONDecodeError,TypeError):
            for match in EMAIL_REGEX.findall(script):
                valid = _clean_and_validate(match)
                if valid:
                    found.add(valid)
    return found
def _extract_body_text(page:Page)->set[str]:
    found:set[str]=set()
    try:
        body_text=page.inner_text('body')
        for match in EMAIL_REGEX.findall(body_text):
            valid=_clean_and_validate(match)
            if valid:
                found.add(valid)
    except Exception as e:
        print(f"something went wrong when scraping email.\nerror: {e}")
        pass
    return found
def extract_emails(page: Page) -> set[str]:
    results: set[str] = set()
    # layer 1 
    results.update(_extract_mailto(page))
    # layer 2
    results.update(_extract_json_ld(page))
    # layer 3
    results.update(_extract_body_text(page))

    return results
# ----- Social link ex
socials=["facebook","instagram","tiktok","twitter"]
def link_extractor(page:Page)->set[str]:
    links:set[str]=set()
    hrefs:list[str]=page.eval_on_selector_all('a[href]','elements=>elements.map(el=>el.getAttribute("href"))')
    for href in hrefs:
        if not href:
            continue
        if any(li in href.lower() for li in socials):
            clean_link=href.strip()
            links.add(clean_link)
    return links