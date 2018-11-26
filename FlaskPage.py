#JERDON HELGESON
#FLASK APP
#Herewegoooooo

#TO RUN: USE FOLLOWING COMMAND IN SHELL IN CURRENT DIRECTORY
#FLASK_APP=FlaskPage.py flask run

import Importer as IMPRT
import PARKSMODEL as MDL

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



@app.route("/more",methods = ["GET","POST"])
def more():
    if request.method == 'POST':
        select = request.form.get('parkSelect')
        print("Park Selected: ",select)
        #if(select == ""):
        #    return render_template('test.html',park = select)
        #else:
        state = request.form['State']
        loc = request.form['Location']
        print("State: ",state,", Location: ",loc)
        park = getMoreParkData(select)
        return render_template('parkStats.html',parkName = select,
                               pLat = park.lat, pLng = park.lng)


@app.route("/Parks",methods=["GET","POST"])
def send():
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
    return render_template("index.html")

if __name__ =="__main__":
    app.run()





def getZoom(mtd):
    """Returns the zoom value for the map"""
    radius = [1600, 800,400,200,100,50,25,10]
    i = 0
    for r in radius:
        if(mtd <= r):
            print("max travel distance:")
            i = i+1
    return i+2

def getPNames(parks):
    """Creates a list of park names"""
    pNames = []
    for p in parks:
        pNames.append(p.name)
    pNames = list(set(pNames))
    return pNames

def getPLatLngs(parks):
    """creates a list of lat lng tuples"""
    pLa = []
    pLo = []
    for p in parks:
        pLa.append(p.lat)
        pLo.append(p.lng)
    pLa = list(set(pLa))
    pLo = list(set(pLo))
    return pLa, pLo

def getPTups(parks):
    """returns a list of park data tuples for parks page"""
    pTups = []
    for p in parks:
        p.setWeatherAndTemp(run = False)
        pTups.append((p.name,p.lat,p.lng,round(p.distance,2),p.state,p.weather))
    pTups = list(set(pTups))
    #print(pTups)
    return pTups

def getMoreParkData(pName):
    """returns in depth data about one park for the more page"""
    park = IMPRT.getPark(pName)
    return park
