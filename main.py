from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from utils import generate_multiple_access, check_access_key

app = Flask(__name__)
app_port = 5000

# Database access
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///access.db'
db = SQLAlchemy(app)


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num_of_keys = request.values.get('numberOfKeys')
        num_of_keys = int(num_of_keys)
        if num_of_keys > 1000000 or num_of_keys < 0:
            return render_template("index.html", title="Dashboard", error="number can't be larger than 1,000,000 or less than 0")

        keys_list = generate_multiple_access(num_of_keys)
        final_list = []
        for x in keys_list:
            what = check_access_key(x)
            print("what:", what)
            final_list.append(what)
        return render_template("index.html", title="Dashboard", keys=final_list)
    return render_template("index.html", title="Dashboard")


@app.route("/checker", methods=['GET', 'POST'])
def checker():
    if request.method == 'POST':
        aws_key = request.values.get('awsKey')
        aws_id = request.values.get('awsID')

        key = []
        key.append(aws_key)
        key.append(aws_id)
        checked = check_access_key(key)
        return render_template("checker.html", title="Checker", keys=checked)
    return render_template("checker.html", title="Checker")


@app.route("/saved")
def saved():
    return render_template("saved.html", title="Saved")


if __name__ == "__main__":
    app.run(port=app_port, debug=True)
