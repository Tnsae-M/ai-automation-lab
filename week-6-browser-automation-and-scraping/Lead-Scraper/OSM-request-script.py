import requests
try:
    city="Addis Ababa"
    header={"User-Agent":"lead-scraper-learning-project/0.1 (https://github.com/Tnsae-M)"}
    url="https://overpass-api.de/api/interpreter"
    query=f"""[out:json];
    area["name:en"='{city}'][boundary='administrative']->.searchArea;
    node['amenity'='cafe'](area.searchArea);
    out body;"""
    req=requests.post(url,data=query,headers=header,timeout=25)
    print(req.json())
except requests.exceptions.RequestException as e:
    print(f"error occured: {e}")