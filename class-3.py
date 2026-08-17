import requests
from bs4 import BeautifulSoup

website_url = "https://pypi.org/"

response = requests.get(website_url)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

heading = soup.find("h1", class_="homepage-banner__title")

print(heading)
print(heading.text)