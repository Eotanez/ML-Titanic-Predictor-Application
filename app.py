# import necessary libraries
from titanic_main import logistic_model_1
# from flask import PyMongo
# from flask_cors import CORS
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# CORS(app)

# app.config["DEBUG"] = True
# app.config["MONGO_URI"] = os.environ["MONGO_URI"]

# mongo = PyMongo(app)
# servicerequests = mongo.db.servicerequests

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train")
def train():
    return render_template("train-model.html")

@app.route("/test")
def test():
    return render_template("test-model.html")

# create form html rendering
@app.route("/send", methods=["GET", "POST"])
def send():

    if request.method == "POST":
        name = request.form["Name"]
        age = request.form["Age"]
        gender = request.form["Gender"]
        fare = request.form["Cost"]
        pclass = request.form["Class"]

        fare = float(eval(fare))
        pclass = float(eval(pclass))
        age = int(eval(age))

        survived = logistic_model_1(age,gender,pclass,fare)
        
        # db.session.add(pet)
        # db.session.commit()
        print(survived)
        if (survived == 0):
            return redirect("/death", code=302)
        else:
            return redirect("/live", code=302)
        

    return render_template("form.html")

@app.route("/death")
def death():
    return render_template("death.html")

@app.route("/live")
def live():
    return render_template("live.html")

if __name__ == "__main__":
    app.run()
