from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import handleResponse as hr




def main():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
    'slug': 'bitcoin'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '460a33bd-0261-4bdc-bbe4-adc18e353006',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    #print(data)
    #return data
    hresponse = hr.handleResponse(data)
    print(hresponse)

    pchange = hresponse['priceChange']
    if pchange < 0:
      print('price went down')
    elif pchange > 0:
      print('price went up')
    else :
      print('price did not change')

    return hresponse




    
      


  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

    #def main():
    #print("Hello World!")

if __name__ == "__main__":
    main()