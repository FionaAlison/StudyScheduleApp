#  Python image
FROM python:3.9-slim

# working directory
WORKDIR /app

# Copying the application files
COPY . .

# Installing dependencies
RUN pip install -r requirements.txt

# application port
EXPOSE 5002

# Seed the database before starting the app
CMD ["python", "app.py"]
