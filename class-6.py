from selenium import webdriver
from selenium.webdriver.common.by import By



# open browser
browser = webdriver.Chrome()
browser.get("https://dreamersacademy.com.bd/")


titles = browser.find_elements(By.CSS_SELECTOR, ".titleline a")



for title in titles:
    print(title.text)