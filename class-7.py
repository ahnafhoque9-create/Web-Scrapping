from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# open browser
browser = webdriver.Chrome()
browser.get("https://dreamersacademy.com.bd/")

# now wait
time.sleep(2)

# now wait for 2 seconds
time.sleep(2)

# now scroll the website
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(2)

browser.quit()