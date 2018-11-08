#Jerdon Helgeson
#PARKSCRAPER
#State Parks Web Scraper

#REFERENCE 1: https://realpython.com/python-web-scraping-practical-introduction/

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pprint
import csv
pp = pprint.PrettyPrinter(indent = 4)


def httpGET(url):
    """
    Gets content at url using http get
    function from REF1
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        print(e)
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise
    function from REF1
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def tagFinder(tag, rawHtml):
    """Takes 2 inputs: rawHtml as (type: bytes), and tag (type: string).
       Converts rawHTML to readable html using BS4 and collects all text contained within matched html tags with tag.
       Returns list of tagText"""
    html = BeautifulSoup(rawHtml, 'html.parser')
    tagText = []
    for t in html.select(tag):
        #print(t.text)
        if(t.text != "National Park Foundation"):
            tagText.append(t.text)
    return tagText
        
    
def runTheTrack():
    """ Inputs: None (hard coded urls).
        calls httpGET on urls until parks are exhausted and calls tagFinder to get tag text
        Returns: list of text contained within given tags    
    """
    url1 = 'https://www.nationalparks.org/explore-parks/all-parks'
    url = "https://www.nationalparks.org/explore-parks/all-parks?page="
    page = 1
    tagText = []
    while(True):
        #url = input("URL PLZ: ") #manual entry url
        #print("URL: ",url)
        if(len(tagText) == 0):
            raw = httpGET(url1)
        else:
            raw = httpGET(url + str(page))
        if(raw == None):
            print("**********\nRAW NONE BREAK\n**********")
            break
        else:
            tempTT = tagFinder("h2", raw)
            if(len(tempTT) == 0):
                print("**********\nEMPTY LIST BREAK\n**********")
                break
            else:
                tagText += tempTT
            page = page + 1
    return tagText

def writeParks(parks):
    """ Input: list of park names
        function to write all park names to a .txt csv file
    """
    with open("parkNames.csv", mode = "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        for p in parks:
            csv_writer.writerow([p])
    csv_file.close()


def main():
    parks = runTheTrack()
    pp.pprint(parks)
    writeParks(parks)


