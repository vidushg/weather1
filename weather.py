

# Program to take a city name as input and return temperature in F

import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?appid=d0c61e2af77bea9ba7f337ad3f0495d6&q="

cityname = input("Where are you? ")
if cityname!="":
	final = url + cityname
	response = requests.get(final)
	jsonobject = response.json()
	print (jsonobject)
	if jsonobject["cod"] != "404":
			info = jsonobject["main"]
			temp = info["temp"]
			fahrenheit = 9.0/5.0 * (temp + 32 - 273)
			print(cityname + " weather : \n" +
					str(int(fahrenheit)) + " degrees Fahrenheit")
	else:
			print(" City Not Found ")
else: 
	print("No")
