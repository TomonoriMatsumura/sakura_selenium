import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(1024, 768))
#display.start()


firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = '/usr/bin/firefox'

driver = webdriver.Firefox(capabilities=firefox_capabilities)
driver.get("https://secure.sakura.ad.jp/vps/#/login?method=ip")

#try:
#    ip_adress = WebDriverWait(driver, 15).until(
#                    EC.presence_of_elemnt_located((By.ID, "ip-id")))


time.sleep(5)

ip_adress = driver.find_element_by_id("ip-id")
ip_adress.send_keys("")

password = driver.find_element_by_id("ip-password")
password.send_keys("")
password.send_keys(Keys.ENTER)

print driver.title

driver.close()
