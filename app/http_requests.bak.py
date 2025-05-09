import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to crawl a website
def web_crawler(url):
    visited = set()

    urls_to_visit = [url]

    while urls_to_visit:
        current_url = urls_to_visit.pop()
        if current_url not in visited:
            visited.add(current_url)
            try:
                response = requests.get(current_url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")

                for link in soup.find_all("a", href=True):
                    href = link.get("href")

                    full_url = urljoin(current_url, href)

                    parsed_url = urlparse(full_url)
                    if parsed_url.scheme in ["http", "https"]:
                        if full_url not in visited:
                            urls_to_visit.append(full_url)

            except requests.exceptions.RequestException as e:
                print("Error while fetching {current_url}: {str(e)}")

    return visited

base_url = "https://bownce.com/robots.txt"
all_urls = web_crawler(base_url)

for url in all_urls:
    print(url)
