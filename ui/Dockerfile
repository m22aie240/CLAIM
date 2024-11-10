# Dockerfile for UI

FROM python:3.9-slim

WORKDIR /app

# Copy application code and dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

# Expose port 5005 and run the application
EXPOSE 5005
CMD ["python", "app.py"]

