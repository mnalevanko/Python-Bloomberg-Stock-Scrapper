import urllib
import json  
import time

#Open and split data
symbolfile = open("StockList.txt")
symbolsListFull = symbolfile.read()
symbolsList = symbolsListFull.split("\n")

#i needs to be instialised
i = 0

#Loop through symbolslist (-1 because of extra line at the end of txt file)
while i < len(symbolsList) - 1:
    #Changing url based on stock symbol
    url = "http://www.bloomberg.com/markets/chart/data/1D/" + symbolsList[i] + ":US"
    htmltext = urllib.urlopen(url)  # Open URL
    data = json.load(htmltext)  # load JSON file (assosiative array)
    datapoints = data["data_values"] #pick specific key from array
    for point in datapoints:
        print "Time: ", point[0], " Price: ", point[1]
    print "The number of points is ", len(datapoints), " Symbol: ", symbolsList[i]
    i += 1
    time.sleep(4)
