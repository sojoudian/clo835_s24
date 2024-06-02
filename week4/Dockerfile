# Stage 1: Build stage
FROM python:3.11-slim as builder

# Set a working directory in the builder stage
WORKDIR /build

# Install build dependencies (if any)
# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies in a layer
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim

# Set the working directory in the final image
WORKDIR /app

# Copy installed packages from the builder
COPY --from=builder /root/.local /root/.local

# Ensure scripts in .local are callable
ENV PATH=/root/.local/bin:$PATH

# Copy the Flask application files
COPY . .

# Expose port 3000 for the application
EXPOSE 3000

# Command to run the Flask application
CMD ["python", "app.py"]
