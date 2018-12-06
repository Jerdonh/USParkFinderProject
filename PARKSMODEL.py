#JERDON HELGESON
#PARKS MODEL

from __future__ import print_function
import requests
import Conversions as CONV
import Weather as WTHR
import datetime as DT
now = DT.datetime.now()


KEY = "AIzaSyAeeM9Ms_AFDC3gOxZixvm4qdgXHf8njFs"
apiURL = "https://maps.googleapis.com/maps/api/geocode/json?address="

class Park:
    """Park Class: reprents a US Park
        -contains working attributes:name,state,yearEstablished,
                                    lat,lng,weather,
                                    currentTemp,distance
        """
    #attributes
    name = "n/a"
    state = "n/a"
    yearEstablished = 0
    lat = 0
    lng = 0
    annualVisitors = 0
    weather = ""
    currentTemp = 0
    distance = 0

    #methods
    def __init__(self, name = None, state = None,
                 lat = None, lng = None, vis = None,
                 wthr = False, dist = None):
        """init method for Park Class:
                required inputs are: name
                                     or name, state, lat, lng """
        if(name != None and state == None and lat == None
           and lng == None and vis == None and wthr == None
           and dist == None):
            self.setParkWithName(name)

        else:
            self.name = name #1
            self.state = state #2
            self.lat = lat #3
            self.lng = lng #4
            self.annualVisitors = vis #5
            if(wthr == True):
                self.setWeather()
                self.setTemp()

    def __eq__(self, other):
        """Overloads == operator to check the name for equality"""
        if(self.name == other.name):
            return True
        else:
            return False

    def __lt__(self, other):
        """Overloads less than operator to compare names alphabetically"""
        return self.name < other.name

    def __gt__(self, other):
        """Overloads greater than operator to compare names alphabetically"""
        return self.name > other.name

    def __le__(self, other):
        """Overloads less than equal operator to compare names alphabetically"""
        return self.name <= other.name

    def __ge__(self, other):
        """Overloads greater than equal operator to compare names alphabetically"""
        return self.name >= other.name
        
    def __cmp__(self, other):
        """Overloads comparison operator to compare names alphabetically"""
        if(self.name > other.name):
            return 1
        elif(self.name < other.name):
            return -1
        else:
            return 0

    def __str__(self):
        """Overloads str to print just park name"""
        return self.name

    def __repr__(self):
        """Overloads repr to print just park name"""
        return self.name
    
    def getDistance(self, user = None, latlng = None):
        """Returns the distance between two entities
           inputs: user - type: User, latlng - type: tuple
           -provided a user: return the distance from the park to the user
           -provided a latlng: return the distance from the park to the latitude and longitude point
        """
        if(user != None):
            lat1 = self.lat; lat2 = user.lat; lng1 = self.lng; lng2 = user.lng
        else:
            lat1 = self.lat; lat2 = latlng[0]; lng1 = self.lng; lng2 = latlng[1]
        #(((lat1 - lat2)**2) + ((lng1 - lng2)**2))**0.5
        kmDist = CONV.distBetweenCoords(lat1,lng1,lat2,lng2)
        mDist = CONV.kmToMiles(kmDist)
        self.distance = round(mDist,2)
        return mDist

    def setWeatherAndTemp(self, run = True):
        """Sets the weather and temperature attributes of the Park obj.
            inputs: run - type: boolean
            -provided a true run input: will set weather and temp attributes using google api
            -provided a false run input: will set weather and temp attributes using arbitrary placeholders
        """
        if(run == True):
            weathTemp = WTHR.getCurrentWeatherandTemp(self.lat,self.lng)
            #print("PARK TEMP: ",weathTemp[1])
        else:
            weathTemp = ("Weather Placeholder", 300000)
        self.weather = weathTemp[0]
        self.currentTemp = weathTemp[1]
    
    def setWeather(self, date = None):
        """Sets weather attribute of the park object
            inputs: n/a
        """
        self.weather = WTHR.getCurrentWeather(self.lat, self.lng)

    def setTemp(self, date = None):
        """Sets currentTemp attribute of the park object
            inputs: n/a
        """
        self.currentTemp = WTHR.getCurrentTemp(self.lat, self.lng)
    




class User:
    """
        User Class: reprents a user of the Program
        -contains working attributes:name,state,addy,
                                    mTD,lat,lng
    """
    def __init__(self,name = None, state = None, addy = None,
                 mTD = None, iS = None,
                 pVD = None, pW = ["Any"], pT = None, tR = None,
                 tSD = (now.month, now.day), tED = (now.month, now.day),
                 oPN = None):
        """Init Method for User Class: Required inputs are: state and addy"""
        if(oPN != None):
            pass
        else:
            self.name = name
            self.state = state
            a = str(addy) + " "+str(state)
            self.setLatLng(a)
            self.inState = iS
            self.maxTravelDistance = mTD
            self.preferredVisitorsDensity = pVD
            self.preferredWeather = pW
            self.preferredTemp = pT
            self.tempRange = tR
            self.travelStartDate = tSD
            self.travelEndDate = tED

    def setLatLng(self, addy):
        """Sets Latitude and Longitude attributes of User obj
            -uses google maps api to obtain lat and lng"""
        request = apiURL + addy + "&key="+KEY
        response = (requests.get(request)).json()
        jsonData = response['results'][0]
        self.lat = jsonData['geometry']['location']['lat']
        self.lng = jsonData['geometry']['location']['lng']
        
    def displayUserDeets(self):
        """Prints all of the attributes of this User object"""
        print("User Information:")
        for d in self.__dict__:
            print("\t",d,": ",self.__dict__[d])


    """
    *******************DEPRACATED -- DEPRACATED -- DEPRACATED********************
    *******************PARK/USER COMPATIBILITY CHECKS****************************
    """
    def checkAbsolutes(self, park):
        """DEPRACATED: This will check the values of a park that determine if it is even eligable to be checked (think distance)"""
        #Check distance
        #print("Park Distance: ", park.getDistance(self))
        #print(self.maxTravelDistance, " < ", park.getDistance(self))
        if((float(park.getDistance(self))) <= (self.maxTravelDistance)):
            #print("\t",park.name, ": is within the range of ", self.name, "'s location", sep = "")
            return True
        else:
            #print("\t",park.name," is not within the travel range")
            return False

    def checkWeather(self, park):
        """DEPRACATED: Blanket method that rates the parks based on their weather"""
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
        """DEPRACATED: Rates a park compared to the user by comparing each of its attributes
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
    
        
        
       
