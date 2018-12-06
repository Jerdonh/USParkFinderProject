#JERDON HELGESON
#IMPORT DATA

import csv
import PARKSMODEL as MDL



def importParks():
    """
        builds and returns a list of park objects from ParksData.csv
    """
    fileName = "ParksData.csv" #"US_Parks_DATA.csv"
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
    year = 3001 #int(items[1])#Old import csv
    state = items[3]
    state = state.strip()
    lat = float(items[1])
    lng = float(items[2])
    visitors = 0 #int(items[5])#Old import csv
    tempPark = MDL.Park(name,state,lat,lng,visitors)
    return tempPark

def getParks(user):
    """
    calls import parks to get list of park objects
    checks parks against user preferences
    returns a list of parks that conform to user preferences
    -inputs: user - type:User
    """
    print("getParks Entered")
    parks = importParks()
    print(len(parks), "parks imported")
    fParks = []
    #print(len(fParks),"initial fParks size")
    #print("Max Travel Dist: ", user.maxTravelDistance)
    for p in parks:
        if(user.checkAbsolutes(p) == True):
            #print(p.name,"Absolute Results == True")
            fParks.append(p)
    #print(len(fParks),"final fParks size")
    return fParks 
    #for p in parks:
    #    print(p)

def getPark(parkName):
    """Returns a single Park obj that matches the input parkName
        -input: parkName - type:String
    """
    parks = importParks()
    for p in parks:
        if(p.name == parkName):
            return p
    return None
    
