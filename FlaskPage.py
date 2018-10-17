#JERDON HELGESON
#FLASK APP
#Herewegoooooo

#TO RUN FOLLOWING COMMAND IN SHELL IN CURRENT DIRECTORY
#FLASK_APP=FlaskPage.py flask run

import Importer as IMPRT
import PARKSMODEL as MDL

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



@app.route("/send",methods=["GET","POST"])
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
        zoom = getZoom(mtd)
        pNames = getPNames(parks)
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
    pTups = []
    for p in parks:
        pTups.append((p.name,p.lat,p.lng))
    pTups = list(set(pTups))
    print(pTups)
    return pTups
