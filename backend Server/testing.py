import requests

a  = requests.post("http://127.0.0.1:5000/flight", json={'entry':'Gandhinagar', 'dest':'Bangalore', 'date':'20191007', 'seats':'2', 'latEn':23.2156, 'lonEn':72.6369, 'latDes':12.9716, 'lonDes':77.5946}).text
print(a)