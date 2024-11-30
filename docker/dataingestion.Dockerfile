# Use the official Python image from the Docker Hub
FROM python:3.11.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the src and scripts directories into the container
COPY src/ /app/src/
COPY src/scripts/ /app/scripts/
COPY alembic.ini /app/

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r /app/requirements.txt
# Ensure the start-dash.sh script is executable
RUN chmod +x /app/scripts/start-dash.sh

# Set the entrypoint to the start-dash.sh script
ENTRYPOINT ["/app/scripts/start-dash.sh"]