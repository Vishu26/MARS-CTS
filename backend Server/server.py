from flask import Flask
from flask import jsonify, request
from fetch import search_buses, search_flights
from func import majorCityFinder

Data = [['Mumbai', 19.0760, 72.8777, 'BOM'],
['Ahmedabad', 23.0225, 72.5714, 'AMD'],
['Vadodara', 22.3072, 73.1812, 'BDQ'],
['Surat', 21.1702, 72.8311, 'STV'],
['Jaipur',  26.9124, 75.7873, 'JAI'],
['Bhopal', 23.2599, 77.4126, 'BHO'],
['Indore',  22.7196, 75.8577, 'IDR'],
['Chennai', 13.0827, 80.2707, 'MAA'],
['Delhi', 28.6139, 77.2090, 'DEL'],
['Lucknow', 26.8467, 80.9462, 'LKO'],
['Calicut', 11.2588, 75.7804, 'CCJ'],
['Hyderabad', 17.3850, 78.4867, 'HYD'],
['Bangalore', 12.9716, 77.5946, 'BLR'],
['Kolkata', 22.5726, 88.3639, 'CCU'],
['Kochi', 9.9312, 76.2673, 'COK'],
['Panaji', 15.4909, 73.8278, 'GOI'],
['Mangaluru', 12.9141, 74.8560, 'IXE'],
['Varanasi', 25.3176, 82.9739, 'VNS'],
['Chandigarh', 30.7333, 76.7794, 'IXC'],
['Amritsar', 31.6340, 74.8723, 'LUH'],
['Siliguri', 26.7271, 88.3953, 'IXB'],
['Coimbatore', 11.0168, 76.9558, 'CJB'],
['Madurai', 9.9252, 78.1198, 'IXM'],
['Tiruchirapalli', 10.7905, 17.7047, 'TRZ'],
['Nagpur', 21.1458, 79.0882, 'NAG'],
['Bhuvneshwar', 20.2961, 85.8245, 'BBI'],
['Vishakhapatnam', 17.6868, 83.2185, 'VTZ'],
['Pune', 18.5204, 73.8567, 'PNQ']]

# Create the application.
APP = Flask(__name__)


@APP.route('/bus', methods=['GET', 'POST'])
def bus():
	data = request.json
	entry = data.get('entry')
	dest = data.get('dest')
	date = data.get('date')
	seats = data.get('seats')
	latEn = data.get('latEn')                                     ## Get current location from front end
	lonEn = data.get('lonEn')
	latDes = data.get('latDes')
	lonDes = data.get('lonDes')
	d = search_buses(entry, dest, date, int(seats))
	if d==-1:
		majorCity1 = majorCityFinder(entry, [latEn, lonEn], Data)  ## Data Load
		majorCity2 = majorCityFinder(dest, [latDes, latDes], Data)
		cas = -1
		if majorCity1[1]==-1 and majorCity2[1]==-1:
			d = search_buses(entry, dest, date, int(seats))
			cas=1
		elif majorCity1[1]==1 and majorCity2[1]==1:
			d = search_buses(majorCity1[0][0], majorCity2[0][0], date, int(seats))
			cas=2
		elif majorCity1[1]==1:
			d = search_buses(majorCity1[0][0], dest, date, int(seats))
			cas=3
		else:
			d = search_buses(entry, majorCity2[0][0], date, int(seats))
			cas=4
		print(d)

		d['majorCity1'] = majorCity1[0][0]
		d['majorCity2'] = majorCity2[0][0]
		d['case'] = cas

	return jsonify(d)

@APP.route('/flight', methods=['GET', 'POST'])
def flight():
	data = request.json
	entry = data.get('entry')
	dest = data.get('dest')
	date = data.get('date')
	seats = data.get('seats')
	latEn = data.get('latEn')                                     ## Get current location from front end
	lonEn = data.get('lonEn')
	latDes = data.get('latDes')
	lonDes = data.get('lonDes')
	majorCity1 = majorCityFinder(entry, [latEn, lonEn], Data)  ## Data Load
	majorCity2 = majorCityFinder(dest, [latDes, latDes], Data)
	print(majorCity1[0][0])
	print(majorCity2[0][0])
	cas = -1
	if majorCity1[1]==-1 and majorCity2[1]==-1:
	### Implement mode
		d = search_flights(majorCity1, majorCity2, date, int(seats))
		cas=1
	elif majorCity1[1]==1 and majorCity2[1]==1:
		d = search_flights(majorCity1, majorCity2, date, int(seats))
		cas=2
	elif majorCity1[1]==1:
		d = search_flights(majorCity1, majorCity2, date, int(seats))
		cas=3
	else:
		d = search_flights(majorCity1, majorCity2, date, int(seats))
		cas=4

	d['majorCity1'] = majorCity1[0][0]
	d['majorCity2'] = majorCity2[0][0]
	d['case'] = cas

	return jsonify(d)

if __name__ == '__main__':
    APP.debug=True
    APP.run()