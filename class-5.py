from selenium import webdriver
import requests
from bs4 import BeautifulSoup

website_link = "https://dreamersacademy.com.bd/"

# open the browser
browser = webdriver.Chrome()

# open the website
browser.get(website_link)

# send request to the website
response = requests.get(website_link)

html_content = response.content