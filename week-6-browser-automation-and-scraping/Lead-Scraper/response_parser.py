from model import LeadModel

def parse_element(element:dict)->LeadModel:
    tags=element.get("tags",{})
    name=tags.get("name") or tags.get("name:en")
    address_list=[tags.get("addr:subcity"),tags.get("addr:street"),tags.get("addr:housenumber")]
    address=",".join(addr for addr in address_list if addr is not None) or None
    phone=tags.get("phone")
    website=tags.get("website")
    email=tags.get("email")
    print(LeadModel(
        name=name,
        address=address,
        email=email,
        phone=phone,
        website=website
    ))