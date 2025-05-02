FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the greetings.py file into the container
COPY greetings.py .

# Set the default command to run the greetings.py script
CMD ["python", "greetings.py"]