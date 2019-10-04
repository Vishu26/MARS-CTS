from flask import Flask
from flask import jsonify, request
from fetch import search_buses


# Create the application.
APP = Flask(__name__)


@APP.route('/bus', methods=['GET', 'POST'])
def index():
	data = request.json
	entry = data.get('entry')
	dest = data.get('dest')
	date = data.get('date')
	seats = data.get('seats')
	print(entry, dest, date, seats)
	d = search_buses(entry, dest, date, int(seats))
	print(d)
	return jsonify(d)

if __name__ == '__main__':
    APP.debug=True
    APP.run()