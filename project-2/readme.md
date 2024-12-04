# Python Application Deployment on Kubernetes

## Overview
This project demonstrates deploying a Python web application that displays the current time in Toronto, Canada, using Docker and Kubernetes.

## Steps to Deploy

Go to MAIN BRANCH

### 1. Build and Run Docker Container

#### Create Dockerfile
1. Create a `Dockerfile` with the following content:
    ```Dockerfile
    # Use the official Python image from the Docker Hub
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Make port 3030 available to the world outside this container
    EXPOSE 3030

    # Define environment variable
    ENV NAME World

    # Run app.py when the container launches
    CMD ["python", "app.py"]
    ```

#### Create requirements.txt
2. Create a `requirements.txt` file with the following content:
    ```text
    Flask==2.0.1
    pytz==2021.1
    ```

#### Build Docker Image
3. Build your Docker image using the following command:
    ```bash
    docker build -t boluadesina/python-app:latest .
    ```

#### Push Docker Image to Docker Hub
4. Push the Docker image to Docker Hub using the following command:
    ```bash
    docker push boluadesina/python-app:latest
    ```

### 2. Deploy on Kubernetes

#### Create Deployment YAML
1. Create a `deployment.yaml` file with the following content:
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: python-app-deployment
      labels:
        app: python-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: python-app
      template:
        metadata:
          labels:
            app: python-app
        spec:
          containers:
          - name: python-app
            image: boluadesina/python-app:latest
            ports:
            - containerPort: 3030
    ```

#### Create Service YAML
2. Create a `service.yaml` file with the following content:
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: python-app-service
    spec:
      type: NodePort
      selector:
        app: python-app
      ports:
        - port: 3030
          targetPort: 3030
          nodePort: 30300
    ```

#### Apply Kubernetes Manifests
3. Apply your Kubernetes manifests using the following commands:
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

### 3. Access the Application
1. Open your web browser and navigate to `http://<NodeIP>:30300`, where `<NodeIP>` is the IP address of one of your Kubernetes nodes.

## Challenges
### Challenge 1: Building the Docker Image
- **Issue**: Encountered errors while building the Docker image due to missing dependencies.
- **Solution**: Ensured that all necessary dependencies were listed in the `requirements.txt` file and used a lightweight base image (`python:3.9-slim`) to reduce the image size.

### Challenge 2: Kubernetes Deployment Issues
- **Issue**: Initial deployment resulted in pods not starting due to incorrect image name.
- **Solution**: Corrected the image name in the `deployment.yaml` file to match the Docker Hub repository.

### Challenge 3: Accessing the Application
- **Issue**: Unable to access the application using the NodePort.
- **Solution**: Verified that the NodePort was correctly configured and used the correct `<NodeIP>` address. Checked firewall settings and ensured ports were open.

## Repository URL
- [GitHub Repository](https://github.com/yourusername/clo835_s24)

## Screenshots
- Include screenshots demonstrating the application running successfully.

## Conclusion
By following these steps, you should be able to deploy a Python application on Kubernetes successfully. This project provided hands-on experience with containerization and orchestration using Docker and Kubernetes.
