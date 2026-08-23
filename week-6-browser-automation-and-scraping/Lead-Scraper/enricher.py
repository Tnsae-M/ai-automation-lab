import re
from urllib.parse import unquote
from playwright.sync_api import Page
import json
from model import LeadModel
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
# ----- Social link extractor
socials=["facebook","instagram","tiktok","twitter","x.com","linkedin"]
def social_links_extractor(page:Page)->set[str]:
    links:set[str]=set()
    hrefs:list[str]=page.eval_on_selector_all('a[href]','elements=>elements.map(el=>el.getAttribute("href"))')
    for href in hrefs:
        if not href:
            continue
        if any(li in href.lower() for li in socials):
            clean_link=href.strip()
            links.add(clean_link)
    return links
def extract_about(page:Page)->str:
    meta_data=page.locator('meta[name="description" i],meta[property="og:description" i]')
    if meta_data.count()>0:
       summary=meta_data.first.get_attribute("content")
       if summary and summary.strip():
           return summary.strip()
    try:
        paragraphs=page.locator('main p, article p, p').all_inner_texts()
        for p in paragraphs:
            clean_p=p.strip()
        if len(clean_p)>40:
            return clean_p[:300]
    except Exception as e:
        print(f'something went wrong when parsing the about!\nerror: {e}')
        pass
    return None
def enrich_model(lead:LeadModel,page:Page):
        try:
            url=lead.website
            if not url:
                print(f"Lead has no website!")
                return None
            page.goto(url=url,wait_until='domcontentloaded',timeout=30000)
            emails=extract_emails(page)
            if emails:
                print("Emails Extraction is complete!")
            social_links=social_links_extractor(page)
            if social_links:
                print("Social links Extraction is complete!")
            about=extract_about(page)
            if about:
                print("About Extraction is complete!")
            lead.email=emails
            lead.social_links=social_links
            lead.about=about
            return lead
        except Exception as e:
            print(f"Something went wrong when enriching lead!\nError: {e}")