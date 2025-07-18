
# Use slim Python image with explicit AMD64 platform
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . .

# Install required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create input and output directories if not already present
RUN mkdir -p input output

# Set entrypoint to run the extractor automatically
CMD ["python", "main.py"]


