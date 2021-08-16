from bs4 import BeautifulSoup
import urllib
import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys

os.chdir('/Users/bennoble/Dropbox/Ben/GitHub/python_summer2021/Day4/Lab/') # set working directory

with open('lab04_ben.csv', 'w') as f: # open new csv file
	w = csv.DictWriter(f, fieldnames = ("name", "title", "email", "website", "specialization")) # set colnames
	w.writeheader() # write header

	# set up selenium stuff
	options = Options()
	options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
	driver_path = '/Users/bennoble/Dropbox/Ben/Keys/chromedriver91'

	# open webpage
	driver = webdriver.Chrome(options = options, executable_path = driver_path)
	driver.get('https://polisci.wustl.edu/people/88/all') # go to website
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to bottom
	time.sleep(5) # pause to let selenium catch up and actually scroll
	html = driver.page_source # get html
	driver.close() # close selenium browser
	soup = BeautifulSoup(html) # soup html

	cards = soup.find_all('a', {'class' : 'card'}) # get all faculty

	for c in range(len(cards)): # for each faculty card
		try:
			fac = {} # empty dict
			fac['name'] = ' '.join(cards[c].find('h3').text.split('\xa0')) # get name, split on weird encoding and re-join
			fac['title'] = cards[c].find('div', {'class' : 'dept'}).text # get title

			interior = 'https://polisci.wustl.edu' + cards[c]['href'] # go to interior page
			interior_page = urllib.request.urlopen(interior) # open interior
			interior_soup = BeautifulSoup(interior_page.read()) # soup interior

			fac['email'] = interior_soup.find('ul', {'class' : 'detail contact'}).find('a').text # get email
			fac['website'] = interior_soup.find('ul', {'class' : 'links'}).find('a')['href'] # get personal website
			fac['specialization'] = interior_soup.find('div', {'class' : 'post-excerpt'}).text # get specialization
			w.writerow(fac) # write row
		except: 
			continue # skip row on issue (e.g., Lee Epstien)
		time.sleep(3) # polite sleep



