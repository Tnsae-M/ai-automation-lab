from model import LeadModel

def parse_element(element:dict)->LeadModel:
    tags=element.get("tags",{})
    name=tags.get("name") or tags.get("name:en")
    address_list=[tags.get("addr:subcity"),tags.get("addr:street"),tags.get("addr:housenumber")]
    address=",".join(addr for addr in address_list if addr is not None) or None
    phone=tags.get("phone")
    website=tags.get("website")
    raw_email=tags.get("email") or tags.get("contact:email")
    email_set={raw_email.strip()} if raw_email else None 
    return LeadModel(
        name=name,
        address=address,
        email=email_set,
        phone=phone,
        website=website,
    )