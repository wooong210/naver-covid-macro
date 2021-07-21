from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os
import random
import pyperclip
import simpleaudio as sa

def ring_a_bell():
    wave_obj = sa.WaveObject.from_wave_file('./ring.wav')
    wave_obj.play()

load_dotenv(verbose=True)
userid = os.getenv("USERID")
password = os.getenv("PASSWORD")

sid = os.getenv("SID2")
orgcode = os.getenv("ORGCODE2")


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
	vactypes = driver.find_element_by_class_name('radio_list')
	print(vactypes.is_displayed())
	if (vactypes.is_displayed()):
		driver.get_screenshot_as_file(f"{time.ctime()}.png")
		vactypes[0].click()
		driver.find_element_by_class_name('label_check')
		driver.find_element_by_id("reservation_confirm")
		ring_a_bell()
	time.sleep(2)
	# driver.refresh()
	driver.execute_script("location.reload()")




time.sleep(10000)
driver.quit()