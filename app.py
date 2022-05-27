from distutils.log import debug
from unicodedata import name
from bson import ObjectId
from flask import Flask, make_response, render_template, request
from pymongo import MongoClient

app = Flask(__name__, template_folder="public", static_folder="public")
app.debug=True
client = MongoClient()
db = client.pastebin

@app.route("/")
def main_page ():
    # notes=["Software engineering Mini Project", "Design and algorithm Presentation", "Cryptography Assingment"," Intellectual property rights LAWS & ORDERS"]
    return render_template ("index.jinja2",notes=db.notes.find())

@app.route("/post", methods=["POST"])
def post():
    db.notes.insert_one(request.json)
    return make_response("OK", 200)

@app.route("/remove", methods=["POST"])
def remove():
    db.notes.delete_one({"_id":ObjectId(request.json["_id"])})
    return make_response("OK", 200)

if __name__ == "__main__":
    app.run()

