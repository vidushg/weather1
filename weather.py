

# Program to take a city name as input and return temperature in F

import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?appid=d0c61e2af77bea9ba7f337ad3f0495d6&q="
locurl="http://api.ipstack.com/check?access_key=01ba0bb834c723d9d47f061780376e45"


print("Do you wish to enter a city or use current location? \n Press 1 for city and 2 for current\n")
choice = input("Enter choice - ")

if choice == "2":

	res = requests.get(locurl)
	locationobj = res.json()

	cityname = locationobj['city']


#Option to choose between detecting user's location and their desired location

elif choice == "1":
	#print (city)
	#cityname = city
	cityname = input("Where are you? ")

else :
	print(choice)
	print("Incorrect input")
	exit

if cityname!="":
	final = url + cityname
	response = requests.get(final)
	jsonobject = response.json()
	#print (jsonobject)
	if jsonobject["cod"] != "404":
			info = jsonobject["main"]
			temp = info["temp"]
			fahrenheit = 9.0/5.0 * (temp + 32 - 273)
			print(cityname + " weather : \n" +
					str(int(fahrenheit)) + " degrees Fahrenheit")
	else:
			print(" City Not Found ")
else: 
	print("Invalid input")
