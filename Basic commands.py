from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver")

driver.get("https://arifu.com/")

print(driver.title)

time.sleep(5)

driver.get("https://arifu.com/")

time.sleep(5)

print(driver.title)

driver.back()

time.sleep(5)

print(driver.title)

driver.forward()

time.sleep(5)

print(driver.title)