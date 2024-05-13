# Python 3.12 image
FROM python:3.12-alpine

# Create a directory in the container, where it will be used
WORKDIR /app

COPY requirements.txt /app/

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory to the WORKDIR directory
COPY . /app
