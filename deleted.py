password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("koko@arifu.com")
password.send_keys("4r1fuD3fault")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
assert isinstance(browser.title, object)
page_title = browser.title
#assert page_title == "pa"
