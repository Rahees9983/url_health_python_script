FROM python:3.11-slim

# Set environment variables to ensure Python outputs everything in stdout and stderr
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "print-logs-console-nd-file.py"]

# Default command to run the script with arguments
CMD ["-c", "/app/env-config.json", "-i", "300"]
