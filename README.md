# Bitcoin Price Notification
Introduction:

As we all know, Bitcoin price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, We are going to get the current price, previous price, and the price change of Bitcoin in real time.


In order to get the latest price for Bitcoin we will be using the Coinmarketcap API. We send an HTTP GET request to the URL('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest) and save the response. Since the API returns a JSON response, we can convert it to a Python object by calling the .json() function on the response. Then we will be using flask to properly display that data. 

We will be using the link at the bottom of the testflask.py file to display our data. In order to access it please follow the web address. 



Project Title
Bitcoin Price Notification


Getting Started
Make sure that you have these five necessary files in your dev. env.  
1. wow.py
2. handleResponse.py
3. testflask.py
4. lastRun.json
5. currentRun.json


Prerequisites
Input the following in your terminal:

pip install json
pip install flask 
pip install python3





Deployment:
1. Run the testflask.py script. 

2. Make sure to run the testflask.py script twice. 

3. follow the web address which will open a page in your browser. 




Built With
Python 
Flask 
Json
Postman

Versioning
version 1.0

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
Thank you to Aedan, Alanna, all of the instructors, TA's, Columbia University and of course the 2021 JTC Spring Cohort. 
