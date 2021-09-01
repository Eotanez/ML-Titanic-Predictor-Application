from flask import Flask, render_template, redirect
from flask import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)
# CORS(app)

app.config["DEBUG"] = True
app.config["MONGO_URI"] = os.environ["MONGO_URI"]

mongo = PyMongo(app)
servicerequests = mongo.db.servicerequests

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

# looking like MapBox isnt needed

# mongodb+srv://titanic_user:<password>@cluster1.1e32k.mongodb.net/myFirstDatabase(Needs to be changed)?retryWrites=true&w=majority