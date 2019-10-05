import requests

#a  = requests.post("http://127.0.0.1:54545/bus", json={'entry':'Bangalore', 'dest':'Gandhinagar', 'date':'07-10-2019', 'seats':'2'}).text
#print(a)
a = requests.post("http://127.0.0.1:54545/locate", json={'entry':'Bangalore', 'dest':'Gandhinagar'})
print(a)