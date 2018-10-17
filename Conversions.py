#JERDON HELGESON
#CONVERSIONS MODULE

R = 6373.0 #radius of planet earth

from math import *

#DISTANCE CONVERSIONS



def distBetweenCoords(lat1, lng1,lat2,lng2):
    """Returns the distance between two coordinates in kilometers"""
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
    return km * 0.621371
    


#TEMPERATURE CONVERSIONS

def kelvinToFarenheit(K):
    F = K * (9/5) - 459.67
    return F

def kelvinToCelcius(K):
    pass

