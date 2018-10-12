#JERDON HELGESON
#ANALYZE PARKS DATA

import GetWeather as WTHR
import PARKSMODEL as MDL
import datetime as DT

now = DT.datetime.now()
tempDate = (now.month,now.day)



"""WEATHER TEST SUITE"""
currentWeather = WTHR.getCurrentWeather(0,0)



"""MODEL TEST SUITE"""
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



