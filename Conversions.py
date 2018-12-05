#JERDON HELGESON
#CONVERSIONS MODULE

R = 6373.0 #radius of planet earth

from math import *
import requests


KEY = "AIzaSyAeeM9Ms_AFDC3gOxZixvm4qdgXHf8njFs"
apiURL = "https://maps.googleapis.com/maps/api/geocode/json?address="

#DISTANCE CONVERSIONS

def getLocToCoords(state = None, loc = None):
    """Returns tuple containing latitude and longitude
    >>> getLocToCoords("Washington","Pullman")
    (46.7297771, -117.1817377)
    """
    a = str(loc) + str(state)
    request = apiURL + a + "&key="+KEY
    response = (requests.get(request)).json()
    jsonData = response['results'][0]
    lat = jsonData['geometry']['location']['lat']
    lng = jsonData['geometry']['location']['lng']
    return (lat,lng)
    

def distBetweenCoords(lat1, lng1,lat2,lng2):
    """Returns the distance between two coordinates in kilometers
    >>> distBetweenCoords(46.72,47.5301,-117.18,-122.0326)
    12219.190593475716
    """
    rlat1 = radians(lat1)
    rlat2 = radians(lat2)
    rlng1 = radians(lng1)
    rlng2 = radians(lng2)
    dlon = abs(rlng2 - rlng1)
    dlat = abs(rlat2 - rlat1)
    
    a = sin(dlat / 2)**2 + cos(rlat1) * cos(rlat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R*c
    return distance
    

def kmToMiles(km):
    """Converts Kilometers to miles: returns miles
        -input: km - type:float
    """
    return km * 0.621371
    


#TEMPERATURE CONVERSIONS

def kelvinToFarenheit(K):
    """Converts Kelvin to Farenheit: returns Farenheit
        -input: K - type:float
    """
    #print("KELVIN: ",K)
    F = (9/5) *(K- 273.15)+32
    #print("FARENHEIT: ",F)
    return F



