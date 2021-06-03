#(in your terminal)export FLASK_APP= 'NAME OF FILE.py'
#
import sqlite3 as sl
#import numpy as np 
import base64
import io
#from matplotlib.figure import Figure
#from flask import Flask, render_template, url_for, send_file
#app = Flask(__name__)


def getcurrentvalues(currency):
  con = sl.connect('crypto.db')
  
  with con:
      ds = con.execute(f"SELECT name, price, volume_24h, timestamp FROM cryptocurrency WHERE name = '{currency}'")
      print(ds.fetchone())
      return ds.fetchone()[1]
    #   for row in ds:
    #     print ('row')
    #     print(row)
    #     print ('row[1]')
    #     print(row[1])




btcprice = getcurrentvalues('Bitcoin')
print(btcprice)

ethprice = getcurrentvalues('Ethereum')
print(ethprice)
