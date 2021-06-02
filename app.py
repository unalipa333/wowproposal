#(in your terminal)export FLASK_APP= 'NAME OF FILE.py'
#
import base64
import io
from matplotlib.figure import Figure
from flask import Flask, render_template, url_for, send_file
app = Flask(__name__)

posts = [
    {
        'crypto': 'Bitcoin',
        'date': '5.04.21',
        'price': '33.33'    },

     {
        'crypto': 'Dogecoin',
        'date': '2.99.21',
        'price': '199.33'    },

     {
        'crypto': 'Etherium',
        'date': '11.23.21',
        'price': '777.33'    }
]

x = 54000
y = 55

@app.route("/")   #decorator and route
@app.route("/home")   #decorator and route
def hello():            #function defined
    return render_template('home.html', posts=posts)  #passing in home.html


@app.route("/btcplot")   #decorator and route
def btcplot():            #function defined
    fig = Figure()
    axs = fig.subplots()
    axs.plot([x, y])
    #ax.set_title('Bitcoin')
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    return send_file(
      io.BytesIO(buf.getvalue()),
      mimetype='image/png'
    )


@app.route("/etherplot")   #decorator and route
def etherplot():            #function defined
    fig = Figure()
    ax = fig.subplots()
    ax.plot([88800, 22222])
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    return send_file(
      io.BytesIO(buf.getvalue()),
      mimetype='image/png'
    )


@app.route("/dogeplot")   #decorator and route
def dogeplot():            #function defined
    fig = Figure()
    ax = fig.subplots()
    ax.plot([88800, 333])
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    return send_file(
      io.BytesIO(buf.getvalue()),
      mimetype='image/png'
    )


# conditional statement so that script can be run directly with python
if __name__ == '__main__':
    app.run(debug=True)    #run in debug mode

