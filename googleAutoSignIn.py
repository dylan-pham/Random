# automated application to sign in to your google account

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\\Users\\Username\\Downloads\\chromedriver.exe') # path to chromedriver.exe
driver.get('https://google.com')
signInButton = driver.find_element_by_id('gb_70')
signInButton.click()
signIn = driver.find_element_by_id('identifierId')
signIn.click()
signIn.send_keys('name@gmail.com') # your email address
signIn.send_keys(Keys.ENTER)
time.sleep(1)
password = driver.find_element_by_name('password')
password.send_keys('password')  # your password
password.send_keys(Keys.ENTER)

# download chromedriver.exe from https://sites.google.com/a/chromium.org/chromedriver/downloads