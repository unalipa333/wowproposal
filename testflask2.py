#(in your terminal)export FLASK_APP= 'NAME OF FILE.py'
#
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'crypto': 'Bitcoin',
        'date': '5.23.21',
        'price': '33.33'    }
]

@app.route("/")   #decorator and route
@app.route("/home")   #decorator and route
def hello():            #function defined
    return render_template('home.html', posts=posts)  #passing in home.html


# conditional statement so that script can be run directly with python
if __name__ == '__main__':
    app.run(debug=True)    #run in debug mode
