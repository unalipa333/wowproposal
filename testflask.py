
import json
import os
from flask import Flask, redirect, url_for 
from wow import main 
#from handleResponse import handleResponse

a = main()

app = Flask(__name__)


@app.route("/")
def home():
    return a 

@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__== "__main__":
    app.run()

