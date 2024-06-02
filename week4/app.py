from flask import Flask, request, jsonify
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

# Connect to MongoDB
mongo_client = MongoClient("mongodb://mongodb:27017")
db = mongo_client['mydb']
collection = db['items']

@app.route('/items', methods=['GET', 'POST'])
def items_handler():
    if request.method == 'GET':
        return get_items()
    elif request.method == 'POST':
        return post_item()
    else:
        return jsonify({"error": "Unsupported request method"}), 405

def get_items():
    items = list(collection.find({}, {'_id': False}))
    return jsonify(items), 200

def post_item():
    try:
        item_data = request.json
        if not item_data:
            raise ValueError("No data provided")
        result = collection.insert_one(item_data)
        item_data['_id'] = str(result.inserted_id)
        return jsonify(item_data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
