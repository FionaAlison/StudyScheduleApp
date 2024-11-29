#!/bin/bash

#  Docker Hub username
DOCKER_USERNAME="fionachebet21932"

# List of microservices and their directories
services=("study-scheduler-service" "motivational-quote-service" "database-service" "frontend-service")

# Function to build and push images
build_and_push() {
    local service_name=$1
    echo "Building and pushing image for $service_name..."
    
    # Navigate to the service directory
    cd ./$service_name || exit
    
    # Build the Docker image
    docker build -t $DOCKER_USERNAME/$service_name:latest .
    
    # Push the Docker image to Docker Hub
    docker push $DOCKER_USERNAME/$service_name:latest
    
    # root directory
    cd ..
}

# Looping through each service and build/push
for service in "${services[@]}"; do
    build_and_push $service
done

echo "All images built and pushed successfully!"
