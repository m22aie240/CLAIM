from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_repository():
    data = request.get_json()
    repo_url = data['repo_url']
    try:
        # Call the Repository Miner Service
        response = requests.post('http://repository-miner-service:5001/clone', json={'repo_url': repo_url})
        
        # Attempt to parse the response as JSON
        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            # Handle non-JSON response
            response_data = {"error": "Invalid JSON response from Repository Miner Service"}

        return jsonify(response_data)
    except requests.exceptions.RequestException as e:
        # Handle connection or request error
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

