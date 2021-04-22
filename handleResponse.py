#import statements
import json
import os


def handleResponse(response):
    #print(response)

    deleteFile("lastRun.json")
    renameFile("currentRun.json", "lastRun.json")
    writeFile("currentRun.json", response)

    currentPrice = response['data']['1']['quote']['USD']['price']
    print(currentPrice)

    lastResponse = readJsonFromFile('lastRun.json')
    previousPrice = lastResponse['data']['1']['quote']['USD']['price']
    print(previousPrice)

    priceChange = currentPrice - previousPrice 
    print(priceChange)

    returnObject = {
        "priceChange": priceChange
    }

    return returnObject

def deleteFile(filename):
    
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

def writeFile(filename, contents):
    with open(filename, 'w') as outfile:
        json.dump(contents, outfile) 

def renameFile(currentName, newName):
    os.rename(currentName, newName)

def readJsonFromFile(filename):
    # Opening JSON file
    f = open(filename, "r")

    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    return data