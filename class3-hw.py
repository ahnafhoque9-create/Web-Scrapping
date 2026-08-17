from selenium import webdriver
import requests
from bs4 import BeautifulSoup

website_link = "https://dreamersacademy.com.bd/"

# Open the browser
browser = webdriver.Chrome()

# Open the website
browser.get(website_link)

# Send request
response = requests.get(website_link)

html_content = response.content


soup = BeautifulSoup(html_content, "html.parser")


heading = soup.find("h1")

print(heading)
print(heading.text)


browser.quit()