from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os
import random
import pyperclip

load_dotenv(verbose=True)
userid = os.getenv("USERID")
password = os.getenv("PASSWORD")

sid = os.getenv("SID")
orgcode = os.getenv("ORGCODE")


# load driver
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(15)

# open site
driver.get(f'https://v-search.nid.naver.com/reservation/standby?orgCd={orgcode}&sid={sid}')
time.sleep(1)

id_element = driver.find_element_by_css_selector("#id")
id_element.click()
time.sleep(random.random() + 1)
pyperclip.copy(userid)
id_element.send_keys(Keys.COMMAND, 'v')

time.sleep(random.random() + 1)

password_element = driver.find_element_by_css_selector("#pw")
password_element.click()
time.sleep(random.random() + 1)
pyperclip.copy(password)
password_element.send_keys(Keys.COMMAND, 'v')
time.sleep(random.random() + 1)

driver.find_element_by_css_selector("#log\.login").click()
time.sleep(1)


driver.find_element_by_css_selector("#ncert > span").click()

time.sleep(10)

while (True):
	vactypes = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/ul").find_elements_by_css_selector(".li")
	print(vactypes)
	if (vactypes):
		# driver.get_screenshot_as_file(f"{time.ctime()}.png") 
		vact = vactypes.find_elements_by_css_selector(".li")
		vact[0].click()
		driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div/label")
		driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/a")
	time.sleep(1)
	driver.refresh()


time.sleep(10000)
driver.quit()