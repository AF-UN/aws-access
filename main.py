from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app_port = 5000

# Database access
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///access.db'
db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Dashboard")


@app.route("/checker")
def checker():
    return render_template("checker.html", title="Checker")


@app.route("/saved")
def saved():
    return render_template("saved.html", title="Saved")


if __name__ == "__main__":
    app.run(port=app_port, debug=True)
