from selenium import webdriver

driver=webdriver.Chrome("/home/nicholas/PycharmProjects/Selenium webtesting/drivers/chromedriver")


###opens chrome and navigates to partner account window
driver.get ("http://partner.arifu.com")
### Maximize window to full view

driver.maximize_window()

driver.find_element_by_id("email").send_keys("koko@arifu.com")

driver.implicitly_wait(60)

driver.find_element_by_id("password").send_keys("4r1fuD3fault")

driver.implicitly_wait(60)

driver.find_element_by_css_selector("#root > div > div > div.isoSignInPage.sc-VigVT.jNAXtR > div > div > form > div:nth-child(3) > div > div > span > button").click()

driver.implicitly_wait(60)

driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]").click()

driver.implicitly_wait(60)

driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/ul/li[1]/a").click()

driver.implicitly_wait(60)

#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/ul/li[2]/a").click()

#driver.implicitly_wait(60)

##click on project dashboard
#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/div/span/span/span").click()

table = driver.find_element_by_xpath('//table')

for row in table.find_elements_by_tag_name('tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(row.text)
        print("********************************************")



#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/ul/li[3]/a").click()

#driver.implicitly_wait(60)

#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/ul/li[3]/a").click()

#driver.implicitly_wait(60)

#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/ul/li[1]/a").click()


###Learner analytics button

#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/section/main/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]").click()

#driver.implicitly_wait(60)

###click on date field

#driver.find_element_by_xpath("//*[@id=\"date-range\"]/span").click()
###Select start date
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[5]/div").click()
###Select end date
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[3]/div").click()

#driver.implicitly_wait(60)

###Click download pdf

#driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/section/section/section/main/div/div/div/div/div/div/div/div[2]/div[3]/div[3]/div[3]/h3/button").click()

###driver.execute_script("window.scrollBy(0,document.body.982px;)","")

###Download program completion rate


###driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/section/section/section/main/div/div/div/div/div/div/div/div[2]/div[3]/div[3]/div[10]/h3/button").click()

#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[3]/a").click()

#driver.implicitly_wait(60)

###driver.find_element_by_link_text("Learner Analytics").click()
#driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/div/header/div/button").click()

#driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/section/section/section/main/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/span").click()
#driver.implicitly_wait(60)

###driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")

###Click on PA account logo
#driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/section/div/header/ul/li[2]/div/img").click()

##driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/
###Log out button

#driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div/a[2]").click()

#print("Test passed")

##driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/div[1]/span/span").click()

##driver.implicitly_wait(60)

##driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/section/section/div/aside/div/section/div[1]/div/ul/li[2]/div/i").click()

##driver.implicitly_wait(60)

##driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div/a[1]").click()

##driver.implicitly_wait(60)

##driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/section/div/header/ul/li[2]/div").click()

#driver.maximize_window()
#driver.close()