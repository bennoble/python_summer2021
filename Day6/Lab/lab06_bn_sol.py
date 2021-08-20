import importlib
import os
import googlemaps

os.chdir('/Users/bennoble/Dropbox/Ben/Keys')
imported_items = importlib.import_module('start_google')
gmaps = imported_items.client


whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

wh = gmaps.geocode(whitehouse)

## 1) closest to WH

def dist_finder(dest, origin = wh):
	orig_lat_long = origin[0]['geometry']['location']
	dist = gmaps.distance_matrix(orig_lat_long, dest)
	kms=[]
	for i in range(3):
		kms.append(float(dist['rows'][0]['elements'][i]['distance']['text'].split(' ')[0]))
	return dest[kms.index(min(kms))]

# find closest embassy
closest = dist_finder(dest = embassies)

# address of closest
closest_address = gmaps.reverse_geocode(closest)[0]['formatted_address']
closest_address

## 2) breakfast place
bfast = gmaps.places_nearby(closest, type = 'cafe', rank_by = "distance", keyword = 'breakfast')['results']

print('Closest breakfast place is {} at {}'.format(bfast[0]['name'], bfast[0]['vicinity'])) # closest

# highest rated
rating = []
for i in range(len(bfast)):
	try:
		rating.append(bfast[i]['rating'])
	except:
		rating.append(0)
best_bfast = bfast[rating.index(max(rating))]

print('Best breakfast place is {} at {}'.format(best_bfast['name'], best_bfast['vicinity'])) # closest

## 5) bar
bars = gmaps.places('bars near ' + '1617 Massachusetts Ave NW, Washington, DC 20036, USA')
dollar = []
for i in range(0, len(bars)):
	try:
	    dollar.append(bars['results'][i]['price_level'])
	except:
	    dollar.append(0)
fancy_bar = bars['results'][dollar.index(max(dollar))]

print('Fanciest bar is {} at {}'.format(fancy_bar['name'], fancy_bar['formatted_address'])) # closest

