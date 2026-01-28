#  Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Create the downloads folder
RUN mkdir -p downloads

# Expose the port Flask runs on
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]