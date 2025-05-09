import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to crawl a website
def web_crawler(sitemap_url):

    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "xml")

        all_urls = [loc.text for loc in soup.find_all("loc")]

        return all_urls

    except requests.exceptions.RequestException as e:
        print("Error while fetching {sitemap_url}: {str(e)}")
        return []

sitemap_url = "https://bownce.com/sitemap.xml"
all_urls = web_crawler(sitemap_url)

for url in all_urls:
    print(url)
