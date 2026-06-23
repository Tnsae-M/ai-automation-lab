import os,sys,requests,logging
from dotenv import load_dotenv
load_dotenv()

def main():
    logger=setup_logger()
    topic=input("Enter the topic u want news from: ").strip()
    api=os.getenv("NEWS_API_KEY")
    if not topic:
        logger.error("Missing topic to search.")
        sys.exit(1)
    if not api:
        logger.error("Missing API key.")
        sys.exit(1)
    filters=input("Enter the filter to sort by(i.e popularity): ")
    if not filters:
        logger.error("Missing filter.")
        sys.exit(1)
    news=get_news(topic,api,filters,logger)
    if news:
        display(news)

def setup_logger():
    fmt="%(asctime)s %(levelname)s: %(message)s"
    dtfmt="%Y-%m-%d %H:%M:%S"
    handler=logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(logging.Formatter(fmt=fmt,datefmt=dtfmt))
    logger=logging.getLogger("news-log")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
def get_news(topic,api,filters,logger):
    url="https://newsapi.org/v2/everything"
    params={
    "apikey":api,
    "q":topic,
    "sortBy":filters
    }
    try:
        res=requests.get(url,params=params,timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as exe:
        logger.error("News fetch failed! %s",exe)
        return None
def display(data):
    articles=data["articles"]
    # instead of print for articles["XX"] use articles.get("XX","No XX"). ex:- articles["title"]
    if articles:
        print(f"Top 5 results!")
        for article in articles[:5]:
            print("-"*25)
            print(f"Article:{article["source"]["name"]}")
            print(f"Author:{article["author"]}")
            print(f"Title:{article["title"]}")
            print(f"Description:{article["description"]}")
            print(f"link to article:{article["url"]}")
            print(f"date of publish:{article["publishedAt"]}")
            print("-"*25)
        else:
            print("No news regarding this topic")
main()