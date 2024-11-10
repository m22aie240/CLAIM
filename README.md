CLAIM (Comprehensive Logic for Analyzing and Identifying Microservices)
CLAIM is a microservices-based application designed to analyze Git repositories, identify microservices, and distinguish infrastructure components from application logic. This project uses a modular architecture with each service performing a specific task, all orchestrated through Docker and Docker Compose.

Project Overview
CLAIM performs the following steps:

Clones the Repository: The Repository Miner Service clones the specified repository.
Parses docker-compose.yml: The File Parser Service identifies and extracts defined services within the docker-compose.yml file.
Classifies Components: The Heuristic Identifier Service classifies each component as either a microservice or an infrastructure component.
Stores Metadata: The Metadata Storage Service saves the structured results in MongoDB for easy retrieval and reference.
Displays Results: The User Interface (UI) provides an easy way to submit repository URLs for analysis and view the results.
Architecture
CLAIM comprises the following microservices:

API Gateway: Centralized service for routing requests and coordinating other services.
Repository Miner Service: Clones the repository and verifies the presence of docker-compose.yml.
File Parser Service: Parses docker-compose.yml files for service definitions.
Heuristic Identifier Service: Applies classification rules to distinguish between microservices and infrastructure components.
Metadata Storage Service (MongoDB): Stores analysis results and allows for retrieval.
User Interface (UI): Web-based interface for submitting URLs and viewing results.
Technology Stack
Programming Language: Python
Database: MongoDB (NoSQL)
Containerization: Docker and Docker Compose
Web Framework: Flask
Getting Started
These instructions will guide you through setting up and running CLAIM on your local machine.

Prerequisites
Docker (latest version)
Docker Compose (latest version)
Git (for repository cloning)
Setup
Clone the Repository:

git clone <repository-url>
cd CLAIM
Build and Start Services: Use Docker Compose to build and start all services.

docker-compose up --build
This command will build and run all services, including the MongoDB container.

Access the UI: Once the services are up and running, open the browser and go to:

http://localhost:5005
Submit a Repository for Analysis:

In the UI, enter a Git repository URL and submit it.
CLAIM will process the repository and display the analysis results, including the classification of each component.
Project Structure
graphql
Copy code
CLAIM/
├── api_gateway/
│   └── app.py             # Main API Gateway code
├── repository_miner/
│   └── repository_miner.py # Clones repositories and locates docker-compose.yml
├── file_parser/
│   └── file_parser.py     # Parses docker-compose.yml for services
├── heuristic_identifier/
│   └── heuristic_identifier.py # Classifies components based on heuristics
├── metadata_storage/
│   └── metadata_storage.py # MongoDB storage and retrieval service
├── ui/
│   └── app.py             # Flask UI application for user interaction
├── docker-compose.yml     # Docker Compose configuration file
└── README.md              # Project documentation
Service Descriptions
API Gateway: Receives user requests, routes them to other services, and returns results.
Repository Miner Service: Clones the specified repository and identifies the docker-compose.yml file.
File Parser Service: Parses docker-compose.yml to identify defined services and their configurations.
Heuristic Identifier Service: Classifies each service as either a microservice or infrastructure.
Metadata Storage Service: Stores analysis results in MongoDB for easy retrieval.
UI: Provides a simple form for users to input a repository URL and displays the results.
API Endpoints
API Gateway
POST /analyze
Description: Initiates the analysis workflow for a given repository URL. Request:
json
Copy code
{
  "repo_url": "https://github.com/example/repository"
}
Response:
json
Copy code
{
  "status": "success",
  "message": "Analysis completed",
  "data": { ... }  // Analysis results
}
Error Handling
If an error occurs during any step, an appropriate message is returned to the UI and displayed to the user. Common errors include:

Repository cloning errors (e.g., invalid repository URL)
Missing docker-compose.yml file
Parsing or classification errors
Cleaning Up
To stop all services and remove the containers:

docker-compose down
To remove all Docker volumes, networks, and images (use with caution):

docker system prune -a
Future Enhancements
Potential future improvements include:

Support for additional SCM platforms (e.g., GitLab, Bitbucket).
Enhanced heuristics for more accurate component classification.
Integration with Kubernetes for advanced scaling and resilience.
CLAIM provides a structured, scalable, and modular solution for analyzing microservices architectures in Git repositories. By leveraging microservices, MongoDB, and Docker, CLAIM ensures flexibility, ease of maintenance, and the potential for future expansion.

Code Author: m22aie240@iitj.ac.in
