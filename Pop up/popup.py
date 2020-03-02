from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver")

driver.maximize_window()
##open htto
driver.get("http://demo.guru99.com/test/delete_customer.php")

driver.implicitly_wait(5)

##Click on submit

driver.find_element_by_name("cusid").send_keys("Wambete")

time.sleep(5)
###Click on submit

driver.find_element_by_name("submit").click()

driver.implicitly_wait(10)

time.sleep(5)

object = driver.switch_to_alert()

msg=object.text
###Print pop up message
print("Alert shows following message: "+msg)

driver.implicitly_wait(10)

object.accept()

driver.quit()
driver.close()