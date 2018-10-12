# GEOCODING US NATIONAL PARKS
# ParkNamesToLAT_LONG V0.1
# JERDON HELGESON
# 9-16-2018
"""PURPOSE: RETRIEVE LATITUDE & LONGITUDE FOR EACH PARK
METHOD: USE GOOGLE MAPS API & GEOCODING FUNCTIONALITY"""

# GOOGLE MAPS API KEY:  AIzaSyAeeM9Ms_AFDC3gOxZixvm4qdgXHf8njFs

import requests
import csv
import time

KEY = "AIzaSyAeeM9Ms_AFDC3gOxZixvm4qdgXHf8njFs"
apiURL = "https://maps.googleapis.com/maps/api/geocode/json?address="
iCSV = 'ParksDataCSV.csv'


#STEP1: Retrieve Addresses

def rowParser(row):
    #print(row)
    sRow = row.split('\t')
    parkName = sRow[0]
    
    state = sRow[2]
    return parkName, state
    

def printListValues(lToPrint):
    for addy in lToPrint:
        print(addy)

#V1: got only addresses
def getAddresses(fileName):
    addressList = []
    with open(fileName, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if(isinstance(row,list)):
                    row = row[0]
            if line_count == 0:
                print('Column names are: ', row)
                line_count += 1
            else:
                parkName,state = rowParser(row)
                parkName = parkName.replace(" ","+")
                state = state.replace(" ","+")
                tempAddress = parkName + "+National+Park,+"+state 
                addressList.append(tempAddress)
                line_count += 1
        print(f'Processed {line_count} lines.')
    #printListValues(addressList)
    csv_file.close()
    return addressList

#STEP2: Format Addresses
    #address format looks like: 1265+NE+Hillside+Dr,+Pullman,+WA
    
testAddress = "1265+NE+Hillside+Dr,+Pullman,+WA"
testAddress2 = "Denali+National+Park,+Alaska"


#STEP3: Convert to Latitude & Longitude

def convertAddresses(addyList):
    latList = []
    lngList = []
    for addy in addyList:
        request = apiURL + addy + "&key="+KEY
        response = (requests.get(request)).json()
        jsonData = response['results'][0]
        #geo = dict()
        lat = jsonData['geometry']['location']['lat']
        print("Latitude:",lat)
        lng = jsonData['geometry']['location']['lng']
        print("Longitude: ",lng)
        address = jsonData['formatted_address']
        latList.append(lat)
        lngList.append(lng)
    return latList,lngList
        

#print(jsonData)


#STEP4: Add latitude & longitude to database

def buildRow(row, lat, lng):
    #newRow = row
    #break up the string here and replace the 3rd and 4th empty spots with lat and lng values
    listRow = row.split(",")
    lrows = len(listRow)
    if(lrows >= 5):
        listRow[3] = str(lat)
        listRow[4] = str(lng)
    else:
        listRow.append(str(lat)+"\t")
        listRow.append(str(lng))
    newRow = ""
    for comp in listRow:
        newRow = newRow + str(comp)
    return newRow
    

def buildNewRows(filename, lats, lngs):
    newRows = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        i = 0
        for row in csv_reader:
            if(isinstance(row,list)):
                row = row[0]
            if line_count == 0:
                newRow = row
            else:
                newRow = buildRow(row,lats[i],lngs[i])
                i = i + 1
            line_count += 1
            newRows.append(newRow)
    csv_file.close()
    return newRows

def toCSV(fileName,newRows):
    with open(fileName, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file)#, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in newRows:
            csv_writer.writerow([row])
        #csv_writer.writerows(newRows)
    csv_file.close()
        


#PSEUDO-MAIN && TESTERS

def runAll():
    addys = getAddresses(iCSV)
    lat,lng = convertAddresses(addys)
    

def testGet():
    addys = getAddresses(iCSV)
    printListValues(addys)

def testConvert():
    addys = getAddresses(iCSV)
    print("ADDRESSES ACQUIRED")
    lats, lngs = convertAddresses(addys)
    print("LATITUDES & LONGITUDES ACQUIRED")
    time.sleep(5)
    printListValues(addys)
    print("\nLATITUDES:\n\n",lats,"LONGITUDES:\n\n",lngs)

def testBuildNewRows():
    addys = getAddresses(iCSV)
    lats, lngs = convertAddresses(addys)
    #i = 0
    #while(i < 60):
    #    lats.append(100)
    #    lngs.append(-100)
    #    i = i+1
    newRows = buildNewRows(iCSV,lats,lngs)
    printListValues(newRows)
    toCSV("test.csv", newRows)

def testBuildNewRows2():
    lats = []
    lngs = []
    i = 0
    while(i < 60):
        lats.append(100)
        lngs.append(-100)
        i = i+1
    newRows = buildNewRows(iCSV,lats,lngs)
    printListValues(newRows)
    toCSV("test.csv",newRows)
    
    
