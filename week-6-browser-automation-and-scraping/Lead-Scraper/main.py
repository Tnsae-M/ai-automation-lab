from osm_request_script import osm_request
from response_parser import parse_element
city=input("Enter City: ")
res= osm_request(city)
print(res)
print("==============")
for element in res["elements"]:
    try:
        parse_element(element)
    except Exception as e:
        print(f"Error occured! Error: {e}")