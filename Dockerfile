FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the greetings.py file into the container
COPY greetings.py .

# Make the script executable
RUN chmod +x /app/greetings.py

# Add /app to the PATH
ENV PATH="/app:${PATH}"

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "/app/greetings.py"]