from selenium import webdriver
import requests
from bs4 import BeautifulSoup

website_link = "https://dreamersacademy.com.bd/"

browser = webdriver.Chrome()
browser.get(website_link)

response = requests.get(website_link)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

headings = soup.find_all("h1")

for heading in headings:
    print(heading.text)

browser.quit()