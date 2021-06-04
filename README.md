# Bitcoin Price Notification
Introduction:

As we all know, Cryptocurrency price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, we are going to get the current price of Bitcoin, Ethereum and Dogecoin in real time and plot this data in a graph on our local machine. The data will be stored using sqlite3. 


In order to get the latest price for Bitcoin we will be using the Coinmarketcap API. We send an HTTP GET request to the URL('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest) and save the response. Since the API returns a JSON response, we can convert it to a Python object by calling the .json() function on the response. Then we will be using flask, matplotlib, bootstrap, html and css to properly display that data. 

We will be using the link at the bottom of the app.py file to display our data. In order to access it please follow the web address. 



Project Title
Bitcoin Price Notification


Getting Started
Make sure that you have these necessary files in your dev. env.  
1. wow.py
2. handleResponse.py
3. app.py
4. lastRun.json
5. currentRun.json
6. home.html (place in folder titled "templates")
7. main.css (place in a folder titled "static")
8. crypto.db



Prerequisites
Input the following in your terminal:

pip install json
pip install flask 
pip install python3
import sqlite3 as sl
import numpy as np 
import base64
import io
from matplotlib.figure import Figure
from flask import Flask, render_template, url_for, send_file





Deployment:


1. Run the app.py script. 
    -be sure to run the wow.py script several times before the app.py in order to populate the table in crypto.db


2. follow the web address to the local page which will appear in your terminal. 

 




Built With
Python 
Flask 
Json
Postman

Versioning
version 1.1

Authors
Maximo Pichardo,
Dorian Brown,
Lyndon Parrilla,
Jesse Roberts,
Brian Kohan,
Mike Bogardino

License
This project is licensed under the JTC cohort under Columbia University 

Acknowledgments
Thank you to Aedan, Alanna, all of the instructors, TA's, Mentors, Columbia University and of course the 2021 JTC Spring Cohort and the cohorts that came before us. 
