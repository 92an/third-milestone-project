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
def get_terms():
    terms = list(mongo.db.terms.find())
    return render_template("terms.html", terms=terms)


@app.route("/add_term")
def add_term():
    return render_template("add_term.html")


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
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check first if there is an existing user with that username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Make a check against the hased password
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Wlcome, {} to EconHub".format(
                        request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # Case if invalid password
                flash("Incorrect username and/or password provided")
                return redirect(url_for("login"))

        else:
            # Case if username is invalid
            flash("Incorrect username and/or password provided")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove session cookie
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
