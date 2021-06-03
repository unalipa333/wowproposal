import unittest as ut
from unittest import result
import os
import sys
import json


from handleResponse import handleResponse, create_connection

class TestHandleResponse(ut.TestCase): 
    #HandleResponse returns unsuccess response object when the quote is invalid or empty
    def test_InvalidQuote(self):
        result = handleResponse('')
        self.assertIsNone(result)

    #HandleResponse returns success response object
    def test_ValidBitcoinQuote(self):
        apiResponse = readJsonFromFile('sampleCoinmarketResponse.json')  #To do replace file name with actual name of crypto json      
        result = handleResponse(apiResponse)
        validReturn = {
            "result": "success"
        }
        self.assertEqual(result, validReturn)

    #createConnection returns a connection when called 
    def test_GoodConnection(self):
        conn =  create_connection('crypto.db')
        self.assertIsNotNone(conn, msg='create_connection is returning None')
        






def readJsonFromFile(filename):
    # Opening JSON file
    f = open(filename, "r")

    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    return data






if __name__ == '__main__':
    ut.main() 


