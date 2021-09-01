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


# looking like MapBox isnt needed