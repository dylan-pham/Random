# automated application to create reminder on Google calendar using selenium module

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def receiveInput():
    reminder = input("Enter reminder: ")
    createReminder(reminder)

def createReminder(reminder):
    driver = webdriver.Chrome('C:\\Users\\Username\\Downloads\\chromedriver.exe') # path to chromedriver.exe 
    driver.get('https://calendar.google.com')

    signIn = driver.find_element_by_id('identifierId')
    signIn.click()
    signIn.send_keys('email@gmail.com') # your email address
    signIn.send_keys(Keys.ENTER)
    time.sleep(1)

    password = driver.find_element_by_name('password')
    password.send_keys('password')  # your password
    password.send_keys(Keys.ENTER)
    time.sleep(1)

    create = driver.find_element_by_class_name('u5sQsb')
    create.click()
    time.sleep(1)

    setTitle = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/content/div/div[1]/div[3]/div/div[1]/div/div[1]/input')
    setTitle.click()
    setTitle.send_keys(reminder)
    time.sleep(1)

    reminderButton = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/content/div/div[1]/div[4]/div[1]/div[2]/content/span')
    reminderButton.click()
    time.sleep(1)

    setAllDay = driver.find_element_by_xpath('//*[@id="tabReminder"]/div/div[2]/div[2]/label/div')
    setAllDay.click()
    setAllDay.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.quit()

receiveInput()

# download chromedriver.exe from https://sites.google.com/a/chromium.org/chromedriver/downloads