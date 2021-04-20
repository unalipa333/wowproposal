from flask import Flask, redirect, url_for 

a = str(4.188989) + ": this is the price of Bitcoin"

app = Flask(__name__)


@app.route("/")
def home():
    return a 

@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__== "__main__":
    app.run()

