from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongo:27017/')
db = client.microservice_data

@app.route('/store', methods=['POST'])
def store_metadata():
    data = request.get_json()
    repo_data = {
        'repository': data['repository'],
        'microservices': data['microservices']
    }
    db.records.insert_one(repo_data)
    return jsonify({'status': 'success'})

@app.route('/retrieve', methods=['GET'])
def retrieve_metadata():
    repository = request.args.get('repository')
    record = db.records.find_one({'repository': repository})
    if not record:
        return jsonify({'error': 'No data found'}), 404
    return jsonify(record)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)

