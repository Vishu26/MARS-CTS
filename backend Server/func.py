from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

def majorCityFinder(name, currLoc, Data):
	closest = 100000
	ret_nm = name
	ind = -1
	for i in enumerate(Data):
		if name==i[1][0]:
			return i[1], -1
		elif distance(currLoc[0], currLoc[1], i[1][1], i[1][2]) < closest:
			closest = distance(currLoc[0], currLoc[1], i[1][1], i[1][2])
			ret_nm = i[1]
			ind = i[0]
	return ret_nm, ind, closest


def nearby3(name, currLoc, Data):
	a = majorCityFinder(name, currLoc, Data)
	Data.pop(a[1])
	b = majorCityFinder(name, currLoc, Data)
	Data.pop(b[1])
	c = majorCityFinder(name, currLoc, Data)
	return a, b, c

def local(dist):
	if dist < 20:
		return "cab", dist*10
	else:
		return "bus", dist*2


