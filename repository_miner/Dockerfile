FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y git && \
    pip install -r requirements.txt

COPY . /app

CMD ["python", "repository_miner.py"]

