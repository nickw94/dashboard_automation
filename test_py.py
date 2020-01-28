from selenium import webdriver
import time

driver = webdriver.Chrome ( "/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver" )
driver.maximize_window()
driver.get("http://www.partner.arifu.com")

driver.find_element_by_name("email").send_keys("koko@arifu.com")

driver.find_element_by_name("password").send_keys("4r1fuD3fault")

driver.find_element_by_css_selector(".btn-flat").click()

time.sleep(10)

driver.close()

