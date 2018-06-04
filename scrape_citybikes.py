import time
import warnings; warnings.filterwarnings('ignore')
from bikelib import *
# TODO1: Amsterdam???
# STEP 1: obtain head reference
bikebase = pd.read_json(BIKE_URL)   #len(bikebase) = 562
#bikebase = bikebase.head()        # limited for now
print('obtained stations for %d systems' %len(bikebase))
# STEP 2: build system dataframe
bikes = process_base(bikebase)  
# STEP 3: populate with bike stations
t0 = time.time()
bikes['data'] = bikes['href'].apply(get_station_data)       # BIG CALL
print('done feeding in %d secs' %(time.time()-t0))
# STEP 4: tabulate additional info for every system
bikes = clean_and_store(bikes)
# STEP 5: compute speeds 
t0 = time.time()
grefs = bikes[bikes['nStations']>20]   # minimum threshold so we can sample 10 trips
hrefs = grefs[['city','country','nStations','stations']]
hrefs['speed'] = grefs.apply(get_distance, axis=1)
hrefs = hrefs[hrefs.speed>0]    # some might fail
hrefs.drop('stations',axis=1,inplace=True)
print('done speeding in %d secs' %(time.time()-t0))
plot_speeds(hrefs)
store_data(hrefs)