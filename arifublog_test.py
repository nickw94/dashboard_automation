###BLOG automation

from selenium import webdriver
import time


driver=webdriver.Chrome("/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver")

driver.get("https://blog.arifu.com/")

driver.maximize_window()

driver.find_element_by_css_selector()


time.sleep(5)

driver.close()
driver.quit()


