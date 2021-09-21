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

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/get_offers")
def get_offers():
    offers = mongo.db.offers.find()
    return render_template("offers.html", offers=offers)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("This email has already been used.")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", email=session["user"]))

    return render_template("register.html")                          


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        
        if existing_email:
            # ensure inserted password matches email input
            if check_password_hash(
                existing_email["password"], request.form.get("password")):
                session["user"] = request.form.get("email")
                flash("Welcome! You are signed in as {}".format(request.form.get("email")))
                return redirect(url_for(
                    "profile", email=session["user"]))
            
            else:
                # invalid password match
                flash("Incorrect email and/or password.")
                return redirect(url_for("signin"))
            
        else:
            # user doesn't exist
            flash("Incorrect email and/or password.")
            return redirect(url_for("signin"))

    return render_template("signin.html") 


@app.route("/profile/<email>", methods=["GET", "POST"])
def profile(email):
    # grab the session user's email from db
    email = mongo.db.users.find_one(
        {"email": session["user"]})["email"]

    if session["user"]:
        return render_template("profile.html", email=email)
    
    return redirect(url_for("signin"))


@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been signed out.")
    session.pop("user")
    return redirect(url_for("signin"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)