import os
import logging
from dotenv import load_dotenv
import requests
import sys
load_dotenv()

def main():
    logger=setup_logger()
    from_curr=input("what is the currency u want to convert from: ").strip()
    to_curr=input("what is the currency u want to convert to: ").strip()
    if not from_curr or not to_curr:
        logger.error("one currency is missing!")
        sys.exit(1)
    amount=int(input("Amount to convert: "))
    if not amount:
        amount=1
    api= os.getenv("CURRENCY_API_KEY")
    if not api:
        logger.error("Api is missing")
        sys.exit(1)
    change=get_currency(from_curr,to_curr,amount,api,logger)
    if change:
        display(change)
def setup_logger():
    fmt="%(asctime)s %(levelname)s: %(message)s"
    dtfmt="%Y-%m-%d %H:%M:%S"
    handler=logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(logging.Formatter(fmt,datefmt=dtfmt))
    logger=logging.getLogger("currency-log")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
def get_currency(curr_from,curr_to,amount,api_key,logger):
    url="http://api.currencylayer.com/convert"
    params={
        'access_key':api_key,
        "from":curr_from,
        "to":curr_to,
        "amount":amount,
    }
    try:
        res=requests.get(url,params=params)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as ex:
        logger.error("Error occured when fetching API: %s",ex)
def display(data):
    query=data["query"]
    result=data["result"]
    print("===CURRENCY change===")
    print(f"{query['amount']} {query['from']} = {result} {query['to']}")

main()
