#JERDON HELGESON
#FLASK APP
#Herewegoooooo

#TO RUN: USE FOLLOWING COMMAND IN SHELL IN CURRENT DIRECTORY
#FLASK_APP=FlaskPage.py flask run

import Importer as IMPRT
import PARKSMODEL as MDL
import Conversions as CONV

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



@app.route("/more",methods = ["GET","POST"])
def more():
    """Renders the stats(more) page of the Website"""
    if request.method == 'POST':
        select = request.form.get('parkSelect')
        print("Park Selected: ",select)
        #if(select == ""):
        #    return render_template('test.html',park = select)
        #else:
        state = request.form['State']
        loc = request.form['Location']
        #print("State: ",state,", Location: ",loc)
        usrLatLng = getUsrLoc(state, loc)
        park = getMoreParkData(select,usrLatLng)
        #print("park: ",park.__dict__)
        return render_template('ParkStats.html',parkName = select,
                               pLat = park.lat, pLng = park.lng,
                               usrLat = usrLatLng[0], usrLng = usrLatLng[1],
                               state = park.state, pDist = park.distance,
                               weath = park.weather, temp = park.currentTemp)


@app.route("/Parks",methods=["GET","POST"])
def send():
    """Renders the main page of the US Parks Finder Website"""
    if request.method == 'POST':
        name = request.form['Name']
        state = request.form['State']
        loc = request.form['Location']
        mtd = int(request.form['maxTravelDistance'])
        user = MDL.User(name,state,loc,float(mtd))
        usrLat = user.lat
        usrLng = user.lng
        parks = IMPRT.getParks(user)
        #print(parks)
        #parks.sort()
        #print(parks)
        zoom = getZoom(mtd)
        pNames = getPNames(parks)
        pNames.sort()
        pLa, pLo = getPLatLngs(parks)
        pTups = getPTups(parks)
        return render_template('test.html', name=name, state=state,
                               location=loc, tdist = mtd,numParks = len(pNames),
                               parks = pNames,usrLat = usrLat, usrLng = usrLng,
                               zoom = zoom, pLa = pLa, pLo = pLo,
                               parkObjs = pTups)
    else:
        return render_template("index.html")
    
@app.route("/back",methods=["GET","POST"])
def back():
    return render_template("index.html")

@app.route("/")
def main():
    """Renders the first page of the US Park Finders website"""
    return render_template("index.html")

if __name__ =="__main__":
    app.run()





def getZoom(mtd):
    """Returns the zoom value for the map
        -input: mtd - type:int
    """
    radius = [1600, 800,400,200,100,50,25,10]
    i = 0
    for r in radius:
        if(mtd <= r):
            print("max travel distance:")
            i = i+1
    return i+2

def getPNames(parks):
    """Creates a list of park names
        -input: parks - type: Park List
    """
    pNames = []
    for p in parks:
        pNames.append(p.name)
    pNames = list(set(pNames))
    return pNames

def getPLatLngs(parks):
    """creates a list of lat lng tuples
        -input: parks - type: Park List
    """
    pLa = []
    pLo = []
    for p in parks:
        pLa.append(p.lat)
        pLo.append(p.lng)
    pLa = list(set(pLa))
    pLo = list(set(pLo))
    return pLa, pLo

def getPTups(parks):
    """returns a list of park data tuples for parks page
        -input: parks - type:string
    """
    pTups = []
    for p in parks:
        p.setWeatherAndTemp(run = False)
        pTups.append((p.name,p.lat,p.lng,round(p.distance,2),p.state,p.weather))
    pTups = list(set(pTups))
    #print(pTups)
    return pTups

def getMoreParkData(pName,usrLatLng):
    """returns in depth data about one park for the more page
        -inputs: pName - type:string, usrLatLng - type:tuple
    """
    park = IMPRT.getPark(pName)
    park.setWeatherAndTemp(run = True)
    park.getDistance(latlng = usrLatLng)
    return park

def getUsrLoc(state, loc):
    """returns tuple containing latitude and longitude
        -inputs: state - type:string, loc - type:string
    """
    latlng = CONV.getLocToCoords(state, loc)
    lat = latlng[0]
    lng = latlng[1]
    return (lat,lng)
