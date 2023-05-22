import sys
import requests
from bs4 import BeautifulSoup
from redis_conn import URLCache
from urllib.parse import urljoin

def link_extractor_logic(given_url):
    res = requests.get(given_url)
    soup=BeautifulSoup(res.text, "html.parser")
    links = []
    for link in soup.find_all('a'):
        links.append({
        "text": " ".join(link.text.split()),
        "href": urljoin(given_url, link.get("href"))
    })
    print(links)
    return links

if __name__ == '__main__':
    given_url = sys.argv[-1]
    link_extractor_logic(given_url)

