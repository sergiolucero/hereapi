# hereapi
python interface to the here.com [REST APIs](https://developer.here.com/develop/rest-apis). 
You must create a developer account at here.com above and set up environment variables HERE_ID and HERE_CODE.

# Example
```
import hereapi

home = [-33.43649,-70.64995]    # Plaza de Armas, Santiago
locs = hereapi.get_isodata(home, 1000,'time')     #1000 seconds
hereapi.isoplot(home, locs,'red','out.html')	# plot in red and save
```
![image](https://user-images.githubusercontent.com/7134649/40279992-c191ac9a-5c1a-11e8-85f6-105445e9f06a.png)

To be fair, the picture above shows 3 concentric isolines (1, 5 and 10 minute drive from my house).

# to be added
* [Truck Routes](https://developer.here.com/documentation/routing/topics/request-a-truck-route.html)
* [Bicycle Routes](https://developer.here.com/documentation/routing/topics/request-a-bicycle-route.html)
* [Map Tiles](https://developer.here.com/documentation/map-tile/topics/quick-start.html)
* [Default Location](https://developer.here.com/documentation/map-image/topics/quick-start-show-default-location.html)
* [Venue Maps](https://developer.here.com/documentation/venue-maps/topics/quick-start.html)
* [GeoCoder](https://developer.here.com/documentation/geocoder/topics/quick-start.html)
* [Weather](https://developer.here.com/documentation/weather/topics/user-guide.html)
* [Transit](https://developer.here.com/documentation/transit/topics/quick-start.html)
