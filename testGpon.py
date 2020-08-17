from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
frames = []
driver = webdriver.Firefox()
driver.get("http://192.168.0.86")

username = driver.find_elements_by_id("userName")
password  = driver.find_element_by_id("pcPassword")
btn = driver.find_element_by_id("loginBtn")
username[0].send_keys("admin")
password.send_keys("admin")
btn.click()
time.sleep(3)

# ids = driver.find_elements_by_id("//[@id='Disconnect']")
# ids = driver.find_elements(By.XPATH,'//*[@id = "mainFrame"]')
# driver.switch_to.frame(driver.find_elements(By.XPATH,'//*[@id = "mainFrame"]'))

# driver.switch_to.frame(driver.find_element_by_tag_name("frameset"))
# print("frame",driver.switch_to.frame(driver.find_element_by_tag_name("frameset")))
for frame in driver.find_elements_by_xpath('.//frame'):
    frames.append(frame)
    
driver.switch_to.frame(frames[2]) 

ids = driver.find_elements_by_id("Disconnect")
# ids = driver.find_element_by_xpath
ids[0].click()
time.sleep(3)
ids_connect = driver.find_elements_by_id("Connect")

