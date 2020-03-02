from selenium import webdriver
import time

driver.maximize_window()

driver.get("http://www.partner.arifu.com")

driver.find_element_by_id("email").send_keys("koko@arifu.com")

driver.find_element_by_id("password").send_keys("4r1fuD3fault")

driver.find_element_by_css_selector("#root > div > div > div.isoSignInPage.sc-VigVT.jNAXtR > div > div > form > div:nth-child(3) > div > div > span > button").click()

driver.find_element_by_css_selector("ant-menu-submenu-title").click()

time.sleep(10)

driver.close()

