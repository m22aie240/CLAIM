from flask import Flask, request, jsonify
import yaml
import requests

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_compose_file():
    data = request.get_json()
    compose_file_content = data['compose_file']
    
    try:
        compose_data = yaml.safe_load(compose_file_content)
        services = compose_data.get('services', {})
    except yaml.YAMLError as e:
        return jsonify({'error': str(e)}), 400

    # Send the parsed services to Heuristic Microservice Identifier
    heuristic_service_url = 'http://heuristic-service:5003/identify'
    response = requests.post(heuristic_service_url, json={'services': services})
    
    return response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

