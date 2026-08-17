
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# setup the browser/driver
browser = webdriver.Chrome()

browser.get("https://practicetestautomation.com/practice-test-login/")

# find the username input box
username_input_box = browser.find_element(By.ID, "username")

# send the username
username_input_box.send_keys("student")

# now for the password
password_input_box = browser.find_element(By.ID, "password")
password_input_box.send_keys("Password123")

time.sleep(2)

# get the login button and click it
login_button = browser.find_element(By.ID, "submit")
login_button.click()

time.sleep(5)

browser.quit()

