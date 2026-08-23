# Lead Scraper

A learning project that finds cafes in a city using OpenStreetMap's Overpass API, then enriches businesses that have a website with publicly available contact and profile information.

## How It Works

1. Prompts for a city name.
2. Queries Overpass for cafe nodes inside the city's administrative boundary.
3. Converts each OpenStreetMap element into a `LeadModel`.
4. Opens each available website in a visible Chromium browser using Playwright.
5. Extracts email addresses, social links, and a short business description.
6. Saves the results as a JSON array in the `leads/` directory.

## Requirements

- Python 3.10 or newer
- Internet access
- Chromium, installed through Playwright

Install the Python dependencies from this directory:

```bash
python -m pip install requests pydantic playwright
python -m playwright install chromium
```

## Run

From the `Lead-Scraper` directory:

```bash
python main.py
```

When prompted, enter a city, for example:

```text
Enter City: Addis Ababa
```

The browser runs in headed mode so website visits are visible. Results are saved to a file named after the entered city, such as `leads/Addis Ababa.json`.

## Supported Cities

The scraper has custom administrative-level mappings for:

- Addis Ababa
- Amsterdam
- Berlin
- Cairo
- Greater London
- Madrid
- Nairobi
- New York
- Paris
- Rome
- Sydney
- Toronto

Other city names use the default administrative level (`4`). OpenStreetMap administrative levels differ by country, so an unknown city may return no results or the wrong area.

## Output

Each lead contains the following fields:

```json
{
  "name": "Example Cafe",
  "address": "Subcity,Street,123",
  "phone": "+123456789",
  "website": "https://example.com",
  "email": ["hello@example.com"],
  "social_links": ["https://www.instagram.com/example"],
  "about": "A short description of the business."
}
```

Fields can be `null` when the source data or website does not provide a value. `email` and `social_links` are sets in Python and are serialized as JSON arrays. Running the scraper for an existing city replaces that city's output file.

## Test Website Enrichment

`test_run.py` checks enrichment against one sample lead instead of querying Overpass:

```bash
python test_run.py
```

## Project Files

- `main.py` - command-line entry point and JSON export
- `osm_request_script.py` - Overpass API request and city mappings
- `response_parser.py` - OpenStreetMap response normalization
- `model.py` - Pydantic lead schema
- `enricher.py` - website crawling and enrichment
- `test_run.py` - standalone enrichment test
- `leads/` - generated city JSON files

## Current Limitations

- This is a V1 script and processes websites sequentially.
- Large city datasets can take a long time and may run into queue or browser-timeout issues.
- Only cafe nodes are queried; other OpenStreetMap cafe element types are not included.
- Website content may be unavailable, block automated browsing, or contain incomplete information.
- Overpass and scraped websites are external services, so requests can fail or be rate-limited.
- Use the collected information responsibly and follow the terms and policies of each service.
