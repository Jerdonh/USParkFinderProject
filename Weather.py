#JERDON HELGESON
#GETWEATHER Module
#GET WEATHER FOR LAT/LNG

#Yahoo Weather Api
#API KEY:dj0yJmk9dEY0dW0xTXd1V2poJmQ9WVdrOVJqQmtTWE5MTjJrbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0zZQ--
#SECRET: 2c8644b4996c8a4311e2a7c40bbd14b63bed0bd2

#open weather map
#API KEY: 75d52627e50e87d56304207f3dbc5a45

import requests
import Conversions as CNVRT

address = "http://api.openweathermap.org/data/2.5/weather?appid=75d52627e50e87d56304207f3dbc5a45&lat="

WeatherTypes = ["Clear","Clouds","Drizzle","Rain","Snow","Thunderstorm"]

def getCurrentWeather(lat, lng):
    url = address + str(lat) + "&lon=" + str(lng)
    json_data = requests.get(url).json()
    currentWeather = json_data['weather'][0]['main']#"Super Stormy Dawg"
    #print()
    #print(currentWeather)
    return currentWeather

def getCurrentTemp(lat, lng):
    url = address + str(lat) + "&lon=" + str(lng)
    json_data = requests.get(url).json()
    currentTemp = json_data['main']['temp']
    currentFTemp = CNVRT.kelvinToFarenheit(currentTemp)
    #print()
    #print(currentFTemp)
    return int(currentFTemp)

def getCurrentWeatherandTemp(lat,lng):
    url = address + str(lat) + "&lon=" + str(lng)
    json_data = requests.get(url).json()
    currentTemp = json_data['main']['temp']
    currentFTemp = CNVRT.kelvinToFarenheit(currentTemp)
    currentWeather = json_data['weather'][0]['main']
    return (currentWeather, currentFTemp)
    
    
