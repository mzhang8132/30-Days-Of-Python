from flask import Flask, render_template, Response, request, redirect, url_for
import json
import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

load_dotenv()

client = pymongo.MongoClient(os.getenv("url"))

db = client.database

@app.route("/cars", methods = ["GET"])
def cars():
    return Response(dumps(db.cars.find()), mimetype = "application/json")

@app.route("/cars/find/<id>", methods = ["GET"])
def car(id):
    car = db.cars.find({"_id": ObjectId(id)})
    return Response(dumps(car), mimetype = "application/json")

@app.route("/cars/create", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        name = request.form["name"]
        make = request.form["make"]
        wheels = int(request.form["wheels"])
        door = int(request.form["door"])
        car = {
            "name": name,
            "make": make,
            "wheels": wheels,
            "doors": door
        }
        db.cars.insert_one(car)
        return redirect(url_for("cars"))
    
@app.route("/cars/update", methods = ["GET", "POST"])
def update():
    if request.method == "GET":
        cars = db.cars.find()
        ids = [str(car["_id"]) for car in cars]
        return render_template("update.html", ids = ids)
    if request.method == "POST":
        id = {"_id": ObjectId(request.form["id"])}
        name = request.form["name"]
        make = request.form["make"]
        wheels = int(request.form["wheels"])
        door = int(request.form["door"])
        car = {
            "name": name,
            "make": make,
            "wheels": wheels,
            "doors": door
        }
        db.cars.update_one(id, {"$set": car})
        return redirect(url_for("car", id = str(id["_id"])))

@app.route("/cars/delete", methods = ["GET", "POST"])
def delete():
    if request.method == "GET":
        cars = db.cars.find()
        ids = [str(car["_id"]) for car in cars]
        names = [car["name"] for car in cars.rewind()]
        makes = [car["make"] for car in cars.rewind()]
        wheels = [car["wheels"] for car in cars.rewind()]
        doors = [car["doors"] for car in cars.rewind()]
        entries = len(ids)
        return render_template("delete.html", entries = entries, ids = ids, names = names, makes = makes, wheels = wheels, doors = doors)
    if request.method == "POST":
        id = ObjectId(request.form["id"])
        db.cars.delete_one({"_id": id})
        return redirect(url_for("delete"))
                       
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True, host = "0.0.0.0", port = port)