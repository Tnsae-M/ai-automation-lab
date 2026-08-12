import requests
def osm_request(city:str):
    try:
        header={"User-Agent":"lead-scraper-learning-project/0.1 (https://github.com/Tnsae-M)"}
        url="https://overpass-api.de/api/interpreter"
        query=f"""[out:json];
        area["name:en"='{city}'][boundary='administrative'][admin_level=4]->.searchArea;
        node['amenity'='cafe'](area.searchArea);
        out body;"""
        req=requests.post(url,data=query,headers=header,timeout=25)
        return req.json()
    except requests.exceptions.RequestException as e:
        print(f"error occured: {e}")
# Be the first user yourself since you will need to reach out to clients to inquire if they need a website and build it for them.
# London admin level=5
print(osm_request("Addis Ababa"))