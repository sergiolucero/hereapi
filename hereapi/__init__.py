import os
import requests
import folium

name = "hereapi"
ID = os.getenv('HERE_ID')
CODE = os.getenv('HERE_CODE')
if ID is None:
	raise Exception('ERROR: please define HERE_ID environment variable')
	
# home =[-33.406654,-70.572701]     # 085 LOS MILITARES / ALONSO DE CORDOVA
heads = {'isoline': 'https://isoline.route.cit.api.here.com/routing/7.2/calculateisoline.json?'}
URL_BASE = {'isoline': '{}app_id={}&app_code={}&mode=shortest;car;traffic:disabled&start=geo!{},{}&range={}&rangetype={}'}

def get_isodata(home, range, type):
	if isinstance(range, (list,array)):		# several values
		comps = [get_isodata(home, rng, type) for rng in range]
	else:
		url = URL_BASE['isoline'].format(heads['isoline'], ID, CODE, home[0],home[1], range, type)
		js = requests.get(url).json()['response']
		# center = js['center']	# {'latitude': -33.406654, 'longitude': -70.572701}
		iso = js['isoline']
		comps = [(float(x.split(',')[0]),float(x.split(',')[1])) for x in iso[0]['component'][0]['shape']]
		
	return comps

def isoplot(home, locations, color, outputfile):
	fm = folium.Map(location = home, zoom_start=13, tiles='CartoDBPositron')
	if isinstance(locations[0][0],float):
		folium.PolyLine(locations=locations,color=color).add_to(fm)
	else:	# a list coming from above (or elsewhere), color is also a list
		for loc,col in zip(locations,color):
			folium.PolyLine(locations=loc,color=col).add_to(fm)
	fm.save(outputfile)s
	print('map saved to %s' %outputfile)