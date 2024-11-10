# app.py

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# The home page with the repository URL input form
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to handle form submission
@app.route('/analyze', methods=['POST'])
def analyze():
    repo_url = request.form['repo_url']
    try:
        # Call the API Gateway's /analyze endpoint
        response = requests.post('http://api-gateway:5000/analyze', json={'repo_url': repo_url})
        response_data = response.json()
        return render_template('index.html', result=response_data)
    except Exception as e:
        return render_template('index.html', result={'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

