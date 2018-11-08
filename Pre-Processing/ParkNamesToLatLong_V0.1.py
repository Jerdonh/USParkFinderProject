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
import pprint
pp = pprint.PrettyPrinter(indent = 4)

KEY = "AIzaSyAeeM9Ms_AFDC3gOxZixvm4qdgXHf8njFs"
apiURL = "https://maps.googleapis.com/maps/api/geocode/json?address="
iCSV = 'ParksDataCSV.csv'
i2CSV = "parkNames.csv"
GLOBstatesAbbrv = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI",
          "IA","ID", "IL","IN","KS","KY","LA","MA","MD","ME","MH","MI","MN",
          "MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY", "OH","OK",
          "OR","PA","PR","PW","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA",
          "WI","WV","WY"]
GLOBstates = ["Alabama","Alaska","Arizona","Arkansas","California",
          "Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii",
          "Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana",
          "Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi",
          "Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey",
          "New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma",
          "Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
          "Tennessee","Texas","Utah","Vermont","Virginia","Washington",
          "West Virginia","Wisconsin","Wyoming","District of Columbia",
          "Puerto Rico","Guam", "American Samoa","U.S. Virgin Islands",
          "Northern Mariana Islands"]


#STEP1: Retrieve Addresses

def rowParser(row):
    #print(row)
    sRow = row.split('\t')
    parkName = sRow[0]
    
    #state = sRow[2]
    return parkName#, state
    

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
            if line_count < 0:
                print('Column names are: ', row)
                line_count += 1
            else:
                parkName = rowParser(row)
                parkName = parkName.replace(" ","+")
                #state = state.replace(" ","+")
                tempAddress = parkName #+ "+National+Park"#,+"+state 
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
    states = []
    requestFails = 0
    for addy in addyList:
        print(addy)
        request = apiURL + addy + "&key="+KEY
        response = (requests.get(request)).json()
        try:
            #pp.pprint(jsonData)
            jsonData = response['results'][0] #jsonData is first element of results: address_components
            lat = jsonData['geometry']['location']['lat']
            print("    Latitude: ",lat)
            lng = jsonData['geometry']['location']['lng']
            print("    Longitude:",lng)
            address = jsonData['formatted_address']
            
            #print("    Address:  ", address.split(','))
            state = ""
            obtainedState = False
            for i in address.split(','):
                    if((obtainedState == False) and (i.strip() in GLOBstatesAbbrv)):
                        state = i.strip()
                        obtainedState = True
                        print("    State:    ", state)
                        break
            if(obtainedState == False):
                addressSplit = address.split(',')
                for i1 in addressSplit:
                    for i in i1.split(" "):
                        if(obtainedState == False and i.strip() in GLOBstatesAbbrv):
                            state = i.strip()
                            obtainedState = True
                            print("    State:    ", state)
                            break
                if(obtainedState == False):
                    print("    *****STATE NOT ACQUIRED*****")              
            
        except Exception as e:
            print("    *************REQUEST FAILED***********")
            print("    Exception: ", e)
            lat = 0.00
            lng = 0.00
            state = ""
            requestFails = requestFails + 1
        
        latList.append(lat)
        lngList.append(lng)
        states.append(state)
    print("Total Request Fails: ", requestFails)
    return latList,lngList, states
        

#print(jsonData)


#STEP4: Add latitude & longitude to database

def buildRow(row, lat, lng, state):
    #newRow = row
    #break up the string here and replace the 3rd and 4th empty spots with lat and lng values
    listRow = row.split(",")
    lrows = len(listRow)
    if(lrows >= 5):
        listRow[3] = str(lat)
        listRow[4] = str(lng)
    else:
        listRow.append(str(lat))
        listRow.append(str(lng))
        listRow.append(str(state))
    newRow = ""
    for comp in listRow:
        newRow = newRow +","+str(comp)
    return newRow[1:]
    

def buildNewRows(filename, lats, lngs,states):
    newRows = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        i = 0
        for row in csv_reader:
            if(isinstance(row,list)):
                row = row[0]
            if line_count < 0:
                newRow = row
            else:
                newRow = buildRow(row,lats[i],lngs[i],states[i])
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
    addys = getAddresses(i2CSV)
    lats,lngs,states = convertAddresses(addys)
    newRows = buildNewRows(i2CSV,lats,lngs,states)
    toCSV("moreParks2.csv", newRows)
    
    

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
    
    
