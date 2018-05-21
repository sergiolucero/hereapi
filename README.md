# hereapi
python interface to the here.com [REST APIs](https://developer.here.com/develop/rest-apis)

# Example
```
import hereapi

home = [-33.43649,-70.64995]    # Plaza de Armas, Santiago
locs = hereapi.get_isodata(home, 1000,'time')     #1000 seconds
hereapi.isoplot(home, locs,'red','out.html')	# plot in red and save
```

# to be added
* [Truck Routes](https://developer.here.com/documentation/routing/topics/request-a-truck-route.html)
* [Bicycle Routes](https://developer.here.com/documentation/routing/topics/request-a-bicycle-route.html)