
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# setup the browser/driver
browser = webdriver.Chrome()

browser.get("https://the-internet.herokuapp.com/login")

# find the username input box
username_input_box = browser.find_element(By.ID, "username")

# send the username
username_input_box.send_keys("tomsmith")

# now for the password
password_input_box = browser.find_element(By.ID, "password")
password_input_box.send_keys("SuperSecretPassword!")

time.sleep(2)

# get the login button and click it
login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(5)

browser.quit()
