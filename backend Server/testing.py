import requests

a  = requests.post("http://127.0.0.1:5000/bus", json={'entry':'Bangalore', 'dest':'Ahmedabad', 'date':'06-10-2019', 'seats':'4'}).text
print(a)