from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("database", 27017)
db = client["password_manager"]
collection = db["users"]

@app.route("/store", methods=["POST"])
def store_password():
    name = request.form.get("name")
    email = request.form.get("email")
    collection.insert_one({"name": name, "email": email})
    return jsonify({"message": "Data stored successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
