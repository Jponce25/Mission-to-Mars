from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# Normal Code
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# However, on my computer for security reasons I require the following code to run including the User and Pass of the MongoDB
# app.config["MONGO_URI"] = "mongodb://user:pass@127.0.0.1:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run(debug=True)