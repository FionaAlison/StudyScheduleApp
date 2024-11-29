# Dockerfile
FROM python:3.8-slim

# working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying the app code
COPY . .

# Exposing port 5001 for the API
EXPOSE 5001

# Run the app
CMD ["python", "app.py"]
