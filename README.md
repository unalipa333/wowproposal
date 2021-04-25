# Bitcoin Price Notification

As we all know, Bitcoin price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, We are going to get the current price, previous price, and the price change of Bitcoin in real time.


In order to get the latest price for Bitcoin we will be using the Coinmarketcap API. We send an HTTP GET request to the URL('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest) and save the response. Since the API returns a JSON response, we can convert it to a Python object by calling the .json() function on the response.