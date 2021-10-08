import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def dounload(url):
	try:
		driver = webdriver.Chrome()
		driver.get(url)
		time.sleep(6)
		objekt = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[4]/div/button")
		url_for_dovnload = objekt.get_attribute('data-download-url')
		name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/span[1]").text
		extention = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/span[2]").text
		weight = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div/div[2]/div/div/div/div[1]/div[1]/div[3]").text
		driver.execute_script(f"window.open('{url_for_dovnload}');")
		message = (f"{name}{extention} || {weight} || start dovnloading from {url}")		
		#print (message)
	except NoSuchElementException:
		message = (f'url: {url} is wrong')
	return message
	

