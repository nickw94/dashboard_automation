###Website automation

from selenium import webdriver

driver=webdriver.Chrome ( "/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver" )

driver.get ("http://arifu.com")

driver.maximize_window()


