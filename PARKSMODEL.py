#JERDON HELGESON
#PARKS MODEL

import GetWeather as WTHR
import datetime as DT
now = DT.datetime.now()

class Park:
    #attributes
    name = "n/a"
    state = "n/a"
    yearEstablished = 0
    lat = 0
    lng = 0
    annualVisitors = 0
    weather = ""
    currentTemp = 0

    #methods
    def __init__(self, name = None, state = None, lat = None, lng = None, vis = None):
        self.name = name #1
        self.state = state #2
        self.lat = lat #3
        self.lng = lng #4
        self.annualVisitors = vis #5
        self.setWeather()
        self.setTemp()
        #self.weather = cw
        #self.currentTemp = ct #7
        
        
    
    def getDistance(self, user):
        """Get the distance between two parks"""
        lat1 = self.lat
        lat2 = user.lat
        lng1 = self.lng
        lng2 = user.lng
        return (((lat1 - lat2)**2) + ((lng1 - lng2)**2))**0.5

    def setWeather(self, date = None):
        self.weather = WTHR.getCurrentWeather(self.lat, self.lng)

    def setTemp(self, date = None):
        self.currentTemp = WTHR.getCurrentTemp(self.lat, self.lng)
         

    def displayParkDeets(self):
        print(self.name," Information: ", sep = "")
        for d in self.__dict__:
            if(d != "name"):
                print("\t",d,": ",self.__dict__[d])
        




class User:
    name: "User"
    state: "n/a"
    lat = 0
    lng = 0
    inState = False
    maxTravelDistance = 0 #in miles
    preferredVisitorsDensity = "Low"
    preferredWeather = []
    preferredTemp = 0
    tempRange = 0
    travelStartDate = (now.month,now.day)
    travelEndDate = (now.month,now.day)

    def __init__(self,name = None, state = None, lat = None, lng = None,
                 iS = None, mTD = None,
                 pVD = None, pW = ["Any"], pT = None, tR = None,
                 tSD = (now.month, now.day), tED = (now.month, now.day)):
        self.name = name
        self.state = state
        self.lat = lat
        self.lng = lng
        self.inState = iS
        self.maxTravelDistance = mTD
        self.preferredVisitorsDensity = pVD
        self.preferredWeather = pW
        self.preferredTemp = pT
        self.tempRange = tR
        self.travelStartDate = tSD
        self.travelEndDate = tED
        
    def displayUserDeets(self):
        print("User Information:")
        for d in self.__dict__:
            print("\t",d,": ",self.__dict__[d])


    """
    *******************PARK/USER COMPATIBILITY CHECKS****************************
    """
    def checkAbsolutes(self, park):
        """This will check the values of a park that determine if it is even eligable to be checked (think distance)"""
        #Check distance
        if(park.getDistance(self) <= self.maxTravelDistance):
            print("\t",park.name, ": is within the range of", self.name, "'s location", sep = "")
            return 0
        else:
            print("\t",park.name," is not within the travel range")
            return -1

    def checkWeather(self, park):
        """Blanket method that rates the parks based on their weather"""
        #Check temperature
        score = 0
        if((park.currentTemp > (self.preferredTemp + self.tempRange))or(park.currentTemp < (self.preferredTemp - self.tempRange))):
            #if the current temp is outside the user's preferred ranges
            score += 1
            difference = 0
            print("\t",park.name, "is not within temperature range", (self.preferredTemp - self.tempRange)," - ",(self.preferredTemp + self.tempRange),sep = "")
            if(park.currentTemp > (self.preferredTemp + self.tempRange)):
                #if park temp is greater than the users preferredTemp + range
                difference = park.currentTemp - (self.preferredTemp + self.tempRange)
            else:
                difference = (self.preferredTemp + self.tempRange) - park.currentTemp
            score += (difference/10)

        else:
            print("i love korina <3 jerdon doesn't even know what he's typing LOL ")
            print("\t",park.name, "is within temperature range",sep = "")

        #Check weather
        if("Any" in self.preferredWeather):
            pass
        elif(park.weather not in self.preferredWeather):
            score += 1
        return score

    def ratePark(self, park):
        """Rates a park compared to the user by comparing each of its attributes
        For each attribute that is not the same add another point to the score.
        Higher scores are less ideal for the user
        If ratePark() returns -1 then the park is disqualified
        """
        score = 0
        #Check Absolutes to see if park is eligible for the list
        score = score + self.checkAbsolutes(park)
        if(score == -1):
            return score
        score = score + self.checkWeather(park)
        #Check visitor density
        
        return score
    
        
        
        
