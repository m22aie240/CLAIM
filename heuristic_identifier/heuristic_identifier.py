from flask import Flask, request, jsonify

app = Flask(__name__)

def is_microservice(service):
    # Heuristics: You can enhance this logic with more complex rules
    if 'image' in service and ('postgres' in service['image'] or 'redis' in service['image']):
        return False  # Likely an infrastructural component
    if 'build' in service:
        return True  # Likely a microservice if there's a build context
    return False

@app.route('/identify', methods=['POST'])
def identify_microservices():
    data = request.get_json()
    services = data['services']
    identified_services = {}

    for service_name, service_info in services.items():
        identified_services[service_name] = 'microservice' if is_microservice(service_info) else 'infrastructure'

    return jsonify(identified_services)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)

