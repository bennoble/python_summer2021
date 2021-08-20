# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 
# for 2 and 3, you will need to enable the google places API
# you may find this page useful to learn about different findinging nearby places https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/


import importlib
import os
import googlemaps

os.chdir('you/key/dir')
imported_items = importlib.import_module('start_google')
gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]
