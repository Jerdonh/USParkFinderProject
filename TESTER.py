#JERDON HELGESON
#ANALYZE PARKS DATA

import Conversions as CONV
import Weather as WTHR
import PARKSMODEL as MDL
import datetime as DT
import Importer as IMPRT

now = DT.datetime.now()
tempDate = (now.month,now.day)
Sloan = (46.731017, -117.169112)
LWorth = (47.596914,-120.661082)


"""WEATHER TEST SUITE"""
currentWeather = WTHR.getCurrentWeather(0,0)


"""CONVERSIONS TEST SUITE"""
def tempTests1():
    K = 280
    F = CONV.kelvinToFarenheit(K)
    print("Kelvin: ", K, ", Farenheit: ",F)

def distTest1():
    d = CONV.distBetweenCoords(Sloan[0],Sloan[1],LWorth[0],LWorth[1])
    d2 = CONV.kmToMiles(d)
    print("Test Distance: ", d2, "miles")

def allCTests():
    tempTests1()
    distTest1()
    


"""MODEL TEST SUITE"""
def modelTest1():
    userTest = MDL.User("Jerdon", "Washington", 46.738904, -117.1604, False,
                    100, "Low", ["Any"], 80, 10, tempDate, tempDate)
    userTest.displayUserDeets()

    parkTest = MDL.Park("Wawawia Park", "Washington", 46.72653, -117.12272,
                    100)

    #parkTest.setWeather()
    parkTest.displayParkDeets()


    print("Park Rating: ")
    score = userTest.ratePark(parkTest)
    print("Park Score: ", score)

def modelDistTest():
    userTest = MDL.User("Jerdon", "Washington", "Pullman",
                    100, False, "Low", ["Any"], 80, 10, tempDate, tempDate)
    parks = IMPRT.getParks(userTest)
    for p in parks:
        print(p.name,"miles from Pullman: " ,p.getDistance(userTest))

def checkAbsolutesTest():
    userTest = MDL.User("Jerdon", "Washington", "Pullman",
                    1000, False, "Low", ["Any"], 80, 10, tempDate, tempDate)
    parks = IMPRT.importParks()
    for p in parks:
        out = userTest.checkAbsolutes(p)
        print(p.name," : ",out)
    

"""importer test suite"""
def importerTest1():
    userTest = MDL.User("Jerdon", "Washington", "Pullman",
                    500, False, "Low", ["Any"], 80, 10, tempDate, tempDate)
    parks = IMPRT.getParks(userTest)
    i = 0
    for p in parks:
        i = i+1
        print(p.name)
    print(i)
    return parks
    


"""CURRENT TEST"""
def c():
    #distTest1()
    #tempTests1()
    #modelTest1()
    importerTest1()
    #modelDistTest()
    #checkAbsolutesTest()
    
