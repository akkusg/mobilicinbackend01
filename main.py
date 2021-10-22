import base64
import datetime
from flask import Flask, jsonify, render_template, request, redirect, session
import pymongo
from bson.json_util import ObjectId
import json


class ObjectIdEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(ObjectIdEncoder, self).default(obj)


app = Flask(__name__)
app.secret_key = 'bizim cok zor gizli sozcugumuz'
app.json_encoder = ObjectIdEncoder

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["YemekDB"]
urunler_tablosu = mydb["urunler"]

@app.route('/')
def index():
    return "Mobil Uygulama için servisler..."

@app.route('/api')
def get_api():
    d = {"res": list(urunler_tablosu.find({}))}
    return jsonify(d)


if __name__ == "__main__":
    app.run(debug=True)