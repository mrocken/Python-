from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://pfsenseip/")
#used when site is untrusted 
driver.find_element_by_id("details-button").click()
driver.find_element_by_id("proceed-link").click()


#main login
username = driver.find_element_by_id("usernamefld")
username.clear()
username.send_keys("username")

password = driver.find_element_by_id("passwordfld")
password.clear()
password.send_keys("password")

driver.find_element_by_css_selector(".btn").click()

#nav to CAmanager 
driver.get("https://pfsenseip/system_camanager.php")


