#(in your terminal)export FLASK_APP= 'NAME OF FILE.py'
#
import base64
from flask import Flask, render_template, url_for
from  matplotlib import pyplot as plt
import mpl_toolkits.axisartist as axisartist
import io
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

@app.route("/")   #decorator and route
@app.route("/home")   #decorator and route
def hello():            #function defined
    return render_template('home.html', posts=posts)  #passing in home.html


# conditional statement so that script can be run directly with python
   #run in debug mode



@app.route("/btcplot", methods='GET') 
def btcplot():
    # Generate the figure **without using pyplot**.
    plt.figure()
    plt.plot([1, 2])
    plt.title("test")
    # Save it to a temporary buffer.
    buf = BytesIO()
    plt.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    


if __name__ == '__main__':
    app.run(debug=True) 



