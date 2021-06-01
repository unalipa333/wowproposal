from flask import Flask, render_template

app = Flask(__name__)       


@app.route("/")
def home():
    data = [
        ("1", 1),
        ("2", 2),
        ("1", 1),
        ("2", 2),
        ("1", 1),
        ("2", 2),
        ("1", 1),
        ("2", 2),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("graph.html", labels=labels, values=values)


if __name__ == '__main__':
    app.run(debug=True) 