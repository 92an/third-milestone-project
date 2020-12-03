import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/get_terms")
def get_term():
    terms = mongo.db.terms.find()
    return render_template("terms.html", terms=terms)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check first if there is an existing user with that username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Flash message if user is found
        if existing_user:
            flash("The username is taken, please choose another")
            return redirect(url_for("register"))

        # Register the user by inserting into database
        user_to_register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(user_to_register)

        # place the new user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration is sucessfull")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
