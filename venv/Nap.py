from selenium import webdriver
import time

driver = webdriver.Chrome ( "/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver" )
driver.maximize_window()
driver.get("http://www.nap.arifu.com")

driver.find_element_by_css_selector(".input-lg").send_keys("koko@arifu.com")

driver.find_element_by_css_selector(".form-item").send_keys("4r1fuD3fault")

driver.find_element_by_css_selector(".btn-flat").click()

print("Complete")

time.sleep(10)

driver.close()


