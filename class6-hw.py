
from selenium import webdriver
from selenium.webdriver.common.by import By


# open browser
browser = webdriver.Chrome()
browser.get("https://dreamersacademy.com.bd/")


headings = browser.find_elements(By.TAG_NAME, "h1")


for heading in headings:
    print(heading.text)

