from selenium import webdriver
river.maximize_window ()
driver.get ( "http://www.partner.arifu.com" )

driver.find_element_by_id (“email”).send_keys ("koko@arifu.com")
driver.find_element_by_id (“password”).send_keys ("4r1fuD3fault")
driver.find_element_by_id (“submit”).click ()

