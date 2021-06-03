#(in your terminal)export FLASK_APP= 'NAME OF FILE.py'
#
import sqlite3 as sl
import numpy as np 
import base64
import io
from matplotlib.figure import Figure
from flask import Flask, render_template, url_for, send_file
app = Flask(__name__)


def getcurrentprice(currency):
  con = sl.connect('crypto.db')
  with con:
      ds = con.execute(f"SELECT name, price, volume_24h, timestamp FROM cryptocurrency WHERE name = '{currency}'")     
      return ds.fetchone()[1]

btcprice = getcurrentprice('Bitcoin')

def getcurrentdate(currency):
  con = sl.connect('crypto.db')
  with con:
      ds = con.execute(f"SELECT name, price, volume_24h, timestamp FROM cryptocurrency WHERE name = '{currency}'")     
      return ds.fetchone()[3]

btcdate = getcurrentdate('Bitcoin')

posts = [
    {
        'crypto': 'Bitcoin',
        'date': btcdate, 
        'price': btcprice, # btcprice
                            },

     {
        'crypto': 'Dogecoin',
        'date': '2.99.21',
        'price': '199.33'    },

     {
        'crypto': 'Ethereum',
        'date': '11.23.21',
        'price': '777.33'    }
]



@app.route("/")   #decorator and route
@app.route("/home")   #decorator and route
def hello():            #function defined
    return render_template('home.html', posts=posts)  #passing in home.html


@app.route("/btcplot2")   #decorator and route
def btcplot():  
    
    return getplot('Bitcoin')


@app.route("/etherplot")   #decorator and route
def etherplot():            #function defined
   
   return getplot('Ethereum')

@app.route("/dogeplot")   #decorator and route
def dogeplot():            #function defined
    
    return getplot('Dogecoin')




def getplot(currency):
    con = sl.connect('crypto.db')
    names = []
    values = []
    #currency = 'Bitcoin'
    with con:
        ds = con.execute(f"SELECT name, price, volume_24h, timestamp FROM cryptocurrency WHERE name = '{currency}'")
        for row in ds:
          names.append(row[3])
          values.append(row[1])          #function defined
    fig = Figure()
    ax = fig.subplots()
    ax.plot(names, values)
    ax.set_xticklabels(ax.get_xticks(), rotation = 90)

    print(names)
    print(values)

    #ax.set_title('Bitcoin')
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    return send_file(
      io.BytesIO(buf.getvalue()),
      mimetype='image/png'
    )



# conditional statement so that script can be run directly with python
if __name__ == '__main__':
  app.run(debug=True)    #run in debug mode

