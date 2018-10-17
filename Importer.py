#JERDON HELGESON
#IMPORT DATA

import csv
import PARKSMODEL as MDL



def importParks():
    fileName = "US_Parks_DATA.csv"
    parks = []
    f = open(fileName,"r")
    i = 0
    for line in f:
        if(i == 0):
            pass
        else:
            park = createPark(line)
            parks.append(park)
        i+=1
    return parks
    
        
        
def createPark(line):
    """turns csv line into park object and returns it"""
    #print(line)
    items = line.split(",")
    #for i in items:
    #    print(i)
    name = items[0]
    year = int(items[1])
    state = items[2]
    lat = float(items[3])
    lng = float(items[4])
    visitors = int(items[5])
    tempPark = MDL.Park(name,state,lat,lng,visitors)
    return tempPark

def getParks(user):
    print("getParks Entered")
    parks = importParks()
    print(len(parks), "parks imported")
    fParks = []
    print(len(fParks),"initial fParks size")
    print("Max Travel Dist: ", user.maxTravelDistance)
    for p in parks:
        if(user.checkAbsolutes(p) == True):
            #print(p.name,"Absolute Results == True")
            fParks.append(p)
    print(len(fParks),"final fParks size")
    return fParks 
    #for p in parks:
    #    print(p)
