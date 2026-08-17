import requests
from bs4 import BeautifulSoup


website_url = "https://www.bbc.com/news"
#https://www.somoynews.tv/

response = requests.get(website_url)
html_content = response.content



soup = BeautifulSoup(html_content,  "html.parser")

print(soup.title)
print(soup.title.string)

