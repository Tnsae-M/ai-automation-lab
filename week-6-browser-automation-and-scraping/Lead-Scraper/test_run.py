from playwright.sync_api import sync_playwright
from enricher import enrich_model
from model import LeadModel
with sync_playwright() as p:
    try:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        test_data='''{
            "name": "Abyssinia Coffee",
            "address": null,
            "phone": "+251 94 410 5183",
            "website": "https://coffeeabyssinia.com/",
            "email": null,
            "social_links": null,
            "about": null
        }'''
        test_data_lead=LeadModel.model_validate_json(test_data)
        print(enrich_model(test_data_lead,page))
        browser.close()
    except Exception as e:
        print(f"sth went wrong!\nError: {e}")
