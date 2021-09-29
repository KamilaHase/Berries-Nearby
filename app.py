import os
import uuid
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

@app.route("/offers")
def offers():
    offers = list(mongo.db.offers.find())
    location = mongo.db.location.find()
    return render_template("offers.html", offers=offers, location=location)


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


@app.route("/add_offer", methods=["GET", "POST"])
def add_offer():
    if request.method == "POST":
        price_free = "on" if request.form.get("price_free") else "off"
        result = None

        if "offer_image" in request.files:
            offer_image = request.files['offer_image']
            if offer_image.filename != '':
                # generate filename using an uuid
                offer_image.filename = str(uuid.uuid4())
                result = mongo.save_file(offer_image.filename, offer_image)

        offers = {
            "category_fruits": request.form.get("category_fruits"),
            "contact": request.form.get("contact"),
            "category_location": request.form.get("category_location"),
            "date_of_pick_up": request.form.get("date_of_pick_up"),
            "description": request.form.get("description"),
            "equipment": request.form.get("equipment"),
            "time_start": request.form.get("time_start"),
            "time_end": request.form.get("time_end"),
            "price_free": price_free,
            "price": request.form.get("price"),
            "offer_image": offer_image.filename,
            "img_id": result,
            "created_by": session["user"]
        }
        mongo.db.offers.insert_one(offers)

        flash("Offer Successfully Added")
        return redirect(url_for("offers"))

    fruit_categories = mongo.db.fruit_categories.find().sort("category_fruits", 1)
    location = mongo.db.location.find().sort("category_location", 1)
    return render_template("add_offer.html", fruit_categories=fruit_categories, location=location)   


@app.route("/edit_offer/<offer_id>", methods=["GET", "POST"])
def edit_offer(offer_id):
    offer = mongo.db.offers.find_one({"_id": ObjectId(offer_id)})
    fruit_categories = mongo.db.fruit_categories.find().sort("category_fruits", 1)
    return render_template("edit_offer.html", offer=offer, fruit_categories=fruit_categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)