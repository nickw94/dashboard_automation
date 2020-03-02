### Dashboard automation.

from selenium import webdriver

driver=webdriver.Chrome ( "/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver" )

driver.get ("http://dashboard.arifu.com")
driver.implicitly_wait(5)

driver.maximize_window()
#find email field and enter email
driver.find_element_by_name ("email").send_keys("nicholas.wambete@arifu.com")
#find password field and enter password
driver.find_element_by_name("password").send_keys("Arifuser")
#find login button and click
driver.find_element_by_css_selector(".btn").click()

driver.implicitly_wait(60)
#Scroll pager to bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")

driver.implicitly_wait(60)
#find drop down menu and click
driver.find_element_by_css_selector(".caret").click()
#find logout button in drop down and click
driver.find_element_by_xpath("/html/body/nav/ul[3]/li[2]/ul/li/a").click()

driver.close()
driver.quit()

print ("Test Complete")
