###Website automation
### update check certificate validation

from selenium import webdriver
import time

driver=webdriver.Chrome ("/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver")

time.sleep(60)

driver.get ("http://arifu.com")

print("https loaded succesfuly")

driver.maximize_window()


driver.find_element_by_css_selector("#menu-nav > li:nth-child(2) > a").click()

print("succesfull click on about button and navigate to page")

driver.implicitly_wait(40)

###driver.find_element_by_css_selector("#menu-nav > li:nth-child(3) > a").click() changed this since davis added the blog option and was generating an error.
###Above code currently woorks but opens a new tab, will focus this to work as part of the blog test scripts

driver.find_element_by_css_selector("#menu-nav > li.current > a").click()

print("succesfull click on partners button and navigate to page")

driver.implicitly_wait(40)

driver.find_element_by_css_selector("#menu-nav > li:nth-child(4) > a").click()

print("succesfull click on impact button and navigate to page")

driver.implicitly_wait(40)

driver.find_element_by_css_selector("#menu-nav > li:nth-child(5) > a").click()

print("succesfull click on team button and navigate to page")

driver.implicitly_wait(40)

#team
driver.find_element_by_css_selector("body").click()

print("succesfull click on team button and navigate to page")


driver.implicitly_wait(40)

#Careers
driver.find_element_by_css_selector("#menu-nav > li:nth-child(7) > a").click()

print("succesfull click on careers button and navigate to page")

driver.implicitly_wait(40)

#Contacts
driver.find_element_by_css_selector("#menu-nav > li:nth-child(8) > a").click()

print("succesfull click on contact button and navigate to page")

driver.find_element_by_name("fname").send_keys("Gabriel")

print("First name populated succesfully")

driver.find_element_by_name("lname").send_keys("Mutua")

print("Last name populated succesfully")

driver.find_element_by_name("company").send_keys("Arifu")

print("company name populated succesfully")

driver.find_element_by_name("email").send_keys("gabriel.mutua@arifu.com")

print("Email field populated succesfully")

driver.find_element_by_name("message").send_keys("Data mining")

print("First name populated succesfully")

driver.find_element_by_name("submit").click()

print("Website test succesful")


time.sleep(20)

driver.close()
driver.quit()

print("Web driver closed")



##driver.find_element_by_css_selector("#aboutin2 > div:nth-child(2) > div > div:nth-child(1) > ul > li > a").click()


#driver.find_element_by_name("recaptcha-checkbox-checkmark").click()
#import time
