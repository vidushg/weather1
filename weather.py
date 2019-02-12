

# Program to take a city name as input and return temperature in F

import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?appid=d0c61e2af77bea9ba7f337ad3f0495d6&q="
locurl="http://api.ipstack.com/check?access_key=01ba0bb834c723d9d47f061780376e45"


#Function takes temp in Kelvin and returns in Fahrenheit
def temp_conv(val):
	return  1.8*(val-273) + 32

#Function takes in choice, and assigns name to cityname accordingly
def assign_cityname(ch):
	if ch == "2":

		res = requests.get(locurl)
		locationobj = res.json()

		return locationobj['city']
	elif ch == "1":

		str = input("Where are you? ")
		return str

	else :

		print("Incorrect input")
		exit

#main function
def main():

	print("Do you wish to enter a city or use current location? \n Press 1 for city and 2 for current\n")
	choice = input("")

	cityname = assign_cityname(choice)

	if cityname!="":
		final = url + cityname
		response = requests.get(final)
		jsonobject = response.json()
		#print (jsonobject)
		#response returns code 404 if city doesn't exist
		if jsonobject["cod"] != "404":
				info = jsonobject["main"]
				temp = info["temp"]
				
				print(jsonobject["name"]+ " weather : \n" +
						str(int(temp_conv(temp))) + " degrees Fahrenheit")
		else:
				print(" City Not Found ")
	else: 
		print("Invalid input")

main()