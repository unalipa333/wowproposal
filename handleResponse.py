#import statements
import sqlite3 as sl 
import json
import os
import sys


def handleResponse(response):
    #ToDo
    #DONE Add the import for SQLite  https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
    #DONE Create a helper function to create a table and call it
    #DONE Extract necessary information from the response
    #DONE Insert data into table
    #DONE Create return object and return it
    #Add exception handling 
        #try:
            #x = int(input("Please   enter a number: "))
            #break
        #except ValueError:
            #print("Oops!  That was no valid number.  Try again...")
    #Add unit test
    #Test Case 1 HandleResponse returns success response object
    #Test Case 2 HandleResponse returns unsuccess response object when the quote is invalid or empty
    #Test Case 3 createConnection returns True when called 
    #Add comment to code
    
    returnObject = None
    
    try:
            



        conn =  create_connection('crypto.db') 
    
        tCreate = CreateTable(conn)
        
        print('tCreate: ', tCreate)
        
        
        
        
        #print(response)

        #deleteFile("lastRun.json")
        #renameFile("currentRun.json", "lastRun.json")
        #writeFile("currentRun.json", response)

        quote = {
            "currentPrice": response['data']['1']['quote']['USD']['price'],
            "name": response['data']['1']['name'],
            "volume_24h": response['data']['1']['quote']['USD']['volume_24h'],
            "timestamp": response['data']['1']['quote']['USD']['last_updated']
        }
        print(quote)


        rInsert = insertData(conn, quote)
        print('rInsert: ', rInsert)


        #lastResponse = readJsonFromFile('lastRun.json')
        #previousPrice = lastResponse['data']['1']['quote']['USD']['price']
        #print(previousPrice)

        #priceChange = currentPrice - previousPrice 
        #print(priceChange)

        returnObject = {
            "result": "success"
        }

    
    except Exception as e:
        print(e)
    
    return returnObject 


def create_connection(db_file):
    #""" create a database connection to the SQLite database
    #   specified by db_file
    #:param db_file: database file
    #:return: Connection object or None
    #"""
    conn = None
    try:
        conn = sl.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return conn

def CreateTable(conn):
    try: 
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cryptocurrency (
                name TEXT,
                price REAL,
                volume_24h REAL,
                timestamp TEXT
                );
            """)
        return True 
    except Exception  as e:
        print(e)
        return False 



def insertData(conn, cryptoData):
    returnVal = None

    print ('cryptoData: ', cryptoData)
    try:
        sql = 'INSERT INTO cryptocurrency (name, price, volume_24h,timestamp) values(?, ?, ?, ?)'
        data = [
            (cryptoData["name"], cryptoData["currentPrice"], cryptoData["volume_24h"], cryptoData["timestamp"]) 
        ]
        print ('data: ', data)
        with conn:
            conn.executemany(sql, data)
        
        returnVal = True

    except Exception as e:
        print('Error: ',e)
        returnVal =  False 
    return returnVal





















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