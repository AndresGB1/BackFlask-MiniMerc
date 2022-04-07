import datetime
import pymongo
from flask import Flask, request, jsonify

# Flask constructor takes the name of
# current module (__name__) as argument
app = Flask(__name__)

# Get the Redis connection
def get_mongo_conn():
    return pymongo.MongoClient("mongodb://localhost:27017")

@app.route("/bus/<busId>/record", methods = ["POST"])
def record(busId):
    m = get_mongo_conn()
    db = m["tm"]
    col = db["telemetry"]
    record = request.json
    record["busId"] = busId
    record["datetime"] = datetime.datetime.now()
    col.insert_one(record)
    return "Record for bus {busId} created successfully".format(busId = busId), 201

@app.route("/archive/speedmax")
def get_speedmax():
    m = get_mongo_conn()
    db = m["tm"]
    col = db["telemetry"]
    limit = int(request.args.get('limit'))
    cursor = col.find({"speed": {"$gte": limit}}, {"_id": 0})
    buses = []
    for bus in cursor:
        buses.append(bus)
    return { "result": buses }

if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()