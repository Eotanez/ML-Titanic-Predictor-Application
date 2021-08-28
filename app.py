# import necessary libraries
from titanic_main import logistic_model_1
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

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("templates/index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["Name"]
        age = request.form["Age"]
        gender = request.form["Gender"]
        fare = request.form["Cost"]
        pclass = request.form["Class"]

        survived = logistic_model_1(age,gender,pclass,fare)

        # db.session.add(pet)
        # db.session.commit()

        if (survived == 0):
            return redirect("/death", code=302)
        else:
            return redirect("/live", code=302)
        

    return render_template("form.html")




if __name__ == "__main__":
    app.run()
