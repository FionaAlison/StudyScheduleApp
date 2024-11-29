# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose service port
EXPOSE 5003

# Start application
CMD ["python", "app.py"]
