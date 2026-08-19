import re
from playwright.sync_api import Page
import json
socials=["facebook","instagram","tiktok","twitter"]
def social_link_extractor(page:Page)->set[str]:
    links:set[str]=set()
    hrefs:list[str]=page.eval_on_selector_all('a[href]','elements=>elements.map(el=>el.getAttribute("href"))')
    for href in hrefs:
        if not href:
            continue
        if any(li in href.lower() for li in socials):
            clean_link=href.strip()
            links.add(clean_link)
    return links