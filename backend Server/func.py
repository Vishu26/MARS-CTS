def majorCityFinder(name, currLoc, Data):
	closest = 100000
	ret_nm = name
	for i in Data:
		if name==i[0]:
			return i, -1
		elif ((currLoc[0]-i[1])**2+(currLoc[1]-i[2])**2)**(0.5) < closest:
			closest = ((currLoc[0]-i[1])**2+(currLoc[1]-i[2])**2)**(0.5)
			ret_nm = i
	return ret_nm, 1