from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def search_buses(a, b, date, seats):
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://bus.makemytrip.com/bus/search/'+a+'/'+b+'/'+date)
	sleep(1)
	try:
		Gbuses = driver.find_element_by_xpath("//a[@class='bluePrimarybtn font12']")
		if Gbuses!=None:
			Gbuses.click()
		sleep(1)
	except:
		pass
	d = dict()
	timing_start = driver.find_elements_by_xpath("//span[@class='sc-gqjmRU izTLmu']")
	timing_duration = driver.find_elements_by_xpath("//span[@class='sc-jzJRlG btSGRi']")
	timing_end = driver.find_elements_by_xpath("//span[@class='sc-fjdhpX laKnSQ']")
	names = driver.find_elements_by_xpath("//span[@class='sc-chPdSV glJpds']")
	types = driver.find_elements_by_xpath("//span[@class='sc-kgoBCf cQRYis']")
	#d['rating'] = driver.find_elements_by_xpath("//span[@class='sc-hSdWYo eXbDWv']")
	cost = driver.find_elements_by_xpath("//span[@class='sc-brqgnP bKUXLW']")
	seats = driver.find_elements_by_xpath("//ul[@class='sc-dxgOiQ BhRgU']")
	#n_state_bus = len(driver.find_elements_by_xpath("//div[@class='sc-kTUwUJ dmMRtR']")[0].find_elements_by_xpath(".//*"))
	#n_pri_bus = len(driver.find_elements_by_xpath("//div[@class='sc-kTUwUJ dmMRtR']")[1].find_elements_by_xpath(".//*"))
	for i in range(len(timing_duration)):
		d[i] = [timing_start[i].text, timing_duration[i].text, timing_end[i].text, names[i].text+types[i].text, cost[i].text, seats[i].text]
	driver.close()
	return d

def search_planes(a, b, date, seats):
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://bus.makemytrip.com/bus/search/'+a+'/'+b+'/'+date)
	sleep(1)
	Gbuses = driver.find_element_by_xpath("//a[@class='bluePrimarybtn font12']")
	if Gbuses!=None:
		Gbuses.click()
	sleep(1)
	timing_start = driver.find_elements_by_xpath("//span[@class='sc-gqjmRU izTLmu']")
	timing_duration = driver.find_elements_by_xpath("//span[@class='sc-jzJRlG btSGRi']")
	timing_end = driver.find_elements_by_xpath("//span[@class='sc-fjdhpX laKnSQ']")
	names = driver.find_elements_by_xpath("//span[@class='sc-chPdSV glJpds']")
	rating = driver.find_elements_by_xpath("//span[@class='sc-hSdWYo eXbDWv']")
	cost = driver.find_elements_by_xpath("//span[@class='sc-brqgnP bKUXLW']")
	seats = driver.find_elements_by_xpath("//ul[@class='sc-dxgOiQ BhRgU']")
	n_state_bus = len(driver.find_elements_by_xpath("//div[@class='sc-kTUwUJ dmMRtR']")[0].find_elements_by_xpath(".//*"))
	n_pri_bus = len(driver.find_elements_by_xpath("//div[@class='sc-kTUwUJ dmMRtR']")[1].find_elements_by_xpath(".//*"))
	driver.close()
	return n_state_bus