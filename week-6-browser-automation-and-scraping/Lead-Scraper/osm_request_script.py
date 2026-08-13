import requests
# admin_level meaning differs by country, not standardized globally.
# Keyed by city (tradeoff: no reuse across cities in same country). possibly use the city of same country's value as a level for another.

# Dubai has admin level 10 but not mentioned because of the name is in arabic and the query uses name, not name:en where some don't have it
# needs more countries in the USA and more!
CITY_ADMIN_LEVELS = {
    "Addis Ababa": 4,"Berlin": 4,"London": 5,"Paris": 6,
    "New York": 5,"Cairo": 4,"Nairobi": 7,"Madrid": 8,"Rome": 8,"Amsterdam": 10,"Toronto": 6,"Sydney": 6,"Dubai":10
}
DEFAULT_ADMIN_LEVEL = 4  # OSM wiki: "first subnational level" for most countries
def osm_request(city:str):
    city=city.strip().title()
    admin_level=CITY_ADMIN_LEVELS.get(city,DEFAULT_ADMIN_LEVEL)
    if city not in CITY_ADMIN_LEVELS:
        print("The city input is not in our current dictionary of city to country admin level mapping. so, if an empty result or any type of error occurs, please verify with the real OSM data in the OSM map and using the admin level there. ")
    try:
        header={"User-Agent":"lead-scraper-learning-project/0.1 (https://github.com/Tnsae-M)"}
        url="https://overpass-api.de/api/interpreter"
        query=f"""[out:json];
        ( area["name"='{city}'][boundary='administrative'][admin_level={admin_level}]; area["name:en"='{city}'][boundary='administrative'][admin_level={admin_level}];)->.searchArea;
        node['amenity'='cafe'](area.searchArea);
        out body;"""
        req=requests.post(url,data=query,headers=header,timeout=25)
        return req.json()
    except requests.exceptions.RequestException as e:
        print(f"error occured: {e}")
# Be the first user yourself since you will need to reach out to clients to inquire if they need a website and build it for them.
print(osm_request("Paris"))