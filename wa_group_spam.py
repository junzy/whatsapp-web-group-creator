###-
###- Web whatsapp python selenium script
###-


### configurations
number_of_times = 10
### List of contact names that match the contacts in your phone

listNames = ['junaid']

### List of group names that are randomly chosen from
listGroups = ['group1', 'group2', 'group3', 'group4']


### Selenium automation
#- download http://chromedriver.storage.googleapis.com/index.html?path=2.21/
#- details https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random


## Selenium web drivers
driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Chrome()
## quit web driver for selenium
def web_driver_quit():
	driver.quit()
	quit()

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	for i in range(0,number_of_times):
		time.sleep(1)
		try:
			createGroup()
		except NoSuchElementException:
			pass
		finally:
			print('Login Checked')

def createGroup():
	while True:
		time.sleep(2)
		print 'Attempting to create group'
		chat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]')
		try:
			chat.click()
		except Exception:
			print 'Could not find matching contact name'
			exit(0)
		time.sleep(2)
		# click on create group
		group = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div[2]/div[1]/div/div[1]/div[2]/div/div')
		group.click()
		time.sleep(2)
		# click on input
		inp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[1]/div/div/input')
		inp.click()
		for name in listNames: 
			inp.send_keys(name)
			time.sleep(0.5)
			inp.send_keys(Keys.RETURN)
		# click on arrow
		arrow = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/span/div/span')
		arrow.click()
		time.sleep(1)
		groupname = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')
		number = random.randint(0,3)
		groupname.send_keys(listGroups[number])
		time.sleep(1)
		groupname.send_keys(Keys.RETURN)
		print 'Group Created'

	exit(0)


### Main Method
if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	for i in range(number_of_times):
		sendMessage(message)
		wait()
	print("Process complete successfully")
	web_driver_quit()
