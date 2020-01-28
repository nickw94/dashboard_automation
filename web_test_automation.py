### Dashboard automation.

from selenium import webdriver

driver=webdriver.Chrome ( "/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver" )

driver.get ("http://dashboard.arifu.com")

driver.maximize_window()

driver.find_element_by_name ("email").send_keys("nicholas.wambete@arifu.com")

driver.find_element_by_name("password").send_keys("Arifuser")

driver.find_element_by_css_selector(".btn").click()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")

driver.find_element_by_css_selector(".caret").click()

driver.find_element_by_xpath("/html/body/nav/ul[3]/li[2]/ul/li/a").click()

driver.close()
driver.quit()

print ("Test Complete")
