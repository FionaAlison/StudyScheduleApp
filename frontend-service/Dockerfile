#  Python runtime as the base image
FROM python:3.9-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements file to the container
COPY requirements.txt .

# Installing the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the application code into the container
COPY . .

# Exposing the Flask port
EXPOSE 5000

# Setting the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Run the Flask application
CMD ["flask", "run"]
