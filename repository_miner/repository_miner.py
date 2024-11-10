from flask import Flask, request, jsonify
import git
import os
import requests

app = Flask(__name__)

@app.route('/clone', methods=['POST'])
def clone_repository():
    data = request.get_json()
    repo_url = data['repo_url']
    
    # Directory to clone the repository
    repo_dir = '/app/repo'
    
    if os.path.exists(repo_dir):
        # Remove old repo if exists
        os.system(f'rm -rf {repo_dir}')
    
    # Clone the repository
    git.Repo.clone_from(repo_url, repo_dir)
    
    # Assume docker-compose.yml is in the root of the repository
    docker_compose_path = os.path.join(repo_dir, 'docker-compose.yml')
    
    if not os.path.exists(docker_compose_path):
        return jsonify({'error': 'docker-compose.yml not found'}), 404
    
    # Send the docker-compose file path to the File Parser service
    file_parser_url = 'http://file-parser-service:5002/parse'
    with open(docker_compose_path, 'r') as file:
        compose_file_content = file.read()
    
    response = requests.post(file_parser_url, json={'compose_file': compose_file_content})
    return response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

