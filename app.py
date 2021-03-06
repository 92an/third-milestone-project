import os
from flask import (
    Flask, flash, render_template, g,
    redirect, request, session, url_for)
from datetime import datetime
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


# creates a global variable that is called
# before request checking if there is a user in session
@app.before_request
def before_request():
    g.user = None

    if "user" in session:
        g.user = session["user"]


@app.route("/")
def homepage():

    if g.user:
        username = session["user"]
        return render_template("homepage.html", username=username)

    return render_template("homepage.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    username = session["user"]
    categories = mongo.db.categories.find().sort("category_name", 1)
    query = request.form.get("query")
    query_category = request.form.get("category_query")

    if len(query) > 0:
        categories = mongo.db.categories.find().sort("category_name", 1)
        terms = list(mongo.db.terms.find({"$text": {"$search": query}}))
        return render_template(
            "terms.html", terms=terms,
            categories=categories, username=username)

    elif query_category != "":
        categories = mongo.db.categories.find().sort("category_name", 1)
        terms = list(mongo.db.terms.find(
            {"$text": {"$search": query_category}}))
        return render_template(
            "terms.html", terms=terms,
            categories=categories, username=username)

    else:
        categories = mongo.db.categories.find().sort("category_name", 1)
        terms = list(mongo.db.terms.find())
        return render_template(
            "terms.html", terms=terms,
            categories=categories, username=username)


""" the following four sections implements CRUD functionallity
to the Economics Dictionary; they are implemented in the
following order: Read, Create, Update and Delete. """


@app.route("/get_terms")
def get_terms():
    username = session["user"]
    terms = list(mongo.db.terms.find())
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "terms.html", terms=terms, categories=categories, username=username)


@app.route("/add_term", methods=["GET", "POST"])
def add_term():
    if request.method == "POST":
        term = {
            "term_name": request.form.get("term_name"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "source_url": request.form.get("source_url"),
            "created_by": session["user"]
        }
        mongo.db.terms.insert_one(term)
        flash("Your term ha been added to the dictonary")
        return redirect(url_for("get_terms"))

    username = session["user"]
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_term.html", categories=categories, username=username)


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
def edit_term(term_id):
    if request.method == "POST":
        term_update = {
            "term_name": request.form.get("term_name"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "source_url": request.form.get("source_url"),
            "created_by": session["user"]
        }
        mongo.db.terms.update({"_id": ObjectId(term_id)}, term_update)
        flash("Term is updated")

    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    username = session["user"]
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_term.html", term=term,  categories=categories, username=username)


@app.route("/delete_term/<term_id>")
def delete_term(term_id):
    mongo.db.terms.remove({"_id": ObjectId(term_id)})
    flash("Term Removed from the Dictionary")
    return redirect(url_for('get_terms'))


"""the following four sections implements CRUD functionallity
to the Categories in the Economics Dictionary; they are implemented in the
following order: Read, Create, Update and Delete. """


@app.route("/manage_categories")
def manage_categories():
    username = session["user"]
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template(
        "categories.html", username=username, categories=categories)


@app.route("/add_category", methods=["POSt", "GET"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Economic Category Added")
        return redirect(url_for("manage_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["POSt", "GET"])
def edit_category(category_id):
    if request.method == "POST":
        category_update = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, category_update)
        flash("Category Updated")
        return redirect(url_for("manage_categories"))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    username = session["user"]
    return render_template(
        "edit_category.html", category=category, username=username)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted")
    return redirect(url_for("manage_categories"))


"""The following 3 sections of code handles user functionallity on the site.
Registration, login, and log out; followed by the
creation of a user profile route which serves as a hub for users"""


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
        terms = list(mongo.db.terms.find())
        return render_template("profile.html", username=username, terms=terms)

    return redirect(url_for("login"))


@app.route("/chattrooms")
def chattrooms():
    username = session["user"]
    return render_template("chattrooms.html", username=username)


# chattroom functions are built below

# chattroom for microeconomics functions are built below
chatt_messages_micro = []


def add_message_micro_chatt(username, message):
    # Populates the list of messages
    now = datetime.now().strftime("%H:%M:%S")
    chatt_messages_dict = {
        "timestamp": now,
        "from": username,
        "message": message
    }
    chatt_messages_micro.append(chatt_messages_dict)


@app.route("/micro_chatt",  methods=["GET", "POST"])
def micro_chatt():
    # add and display messages to screen

    if request.method == "POST":
        username = session["user"]
        message = request.form.get("message_box")
        add_message_micro_chatt(username, message)
        chatt = chatt_messages_micro
        return redirect(url_for("micro_chatt"))

    chatt = chatt_messages_micro
    username = session["user"]
    return render_template(
        "micro_chatt.html", username=username, chatt=chatt)


# chattroom for macroeconomics functions are built below
chatt_messages_macro = []


def add_message_macro_chatt(username, message):
    # Populates the list of messages
    now = datetime.now().strftime("%H:%M:%S")
    chatt_messages_dict = {
        "timestamp": now,
        "from": username,
        "message": message
    }
    chatt_messages_macro.append(chatt_messages_dict)


@app.route("/macro_chatt",  methods=["GET", "POST"])
def macro_chatt():
    # add and display messages to screen

    if request.method == "POST":
        username = session["user"]
        message = request.form.get("message_box")
        add_message_macro_chatt(username, message)
        chatt = chatt_messages_macro
        return redirect(url_for("macro_chatt"))

    chatt = chatt_messages_macro
    username = session["user"]
    return render_template(
        "macro_chatt.html", username=username, chatt=chatt)


# chattroom for political economy functions are built below
chatt_messages_political = []


def add_message_political_chatt(username, message):
    # Populates the list of messages
    now = datetime.now().strftime("%H:%M:%S")
    chatt_messages_dict = {
        "timestamp": now,
        "from": username,
        "message": message
    }
    chatt_messages_political.append(chatt_messages_dict)


@app.route("/political_chatt",  methods=["GET", "POST"])
def political_chatt():
    # add and display messages to screen

    if request.method == "POST":
        username = session["user"]
        message = request.form.get("message_box")
        add_message_macro_chatt(username, message)
        chatt = chatt_messages_political
        return redirect(url_for("political_chatt"))

    chatt = chatt_messages_political
    username = session["user"]
    return render_template(
        "political_chatt.html", username=username, chatt=chatt)


# chattroom for students functions are built below
chatt_messages_student = []


def add_message_student_chatt(username, message):
    # Populates the list of messages
    now = datetime.now().strftime("%H:%M:%S")
    chatt_messages_dict = {
        "timestamp": now,
        "from": username,
        "message": message
    }
    chatt_messages_student.append(chatt_messages_dict)


@app.route("/student_chatt",  methods=["GET", "POST"])
def student_chatt():
    # add and display messages to screen

    if request.method == "POST":
        username = session["user"]
        message = request.form.get("message_box")
        add_message_student_chatt(username, message)
        chatt = chatt_messages_student
        return redirect(url_for("student_chatt"))

    chatt = chatt_messages_student
    username = session["user"]
    return render_template(
        "student_chatt.html", username=username, chatt=chatt)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
