FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Reduce image size by avoiding extra cache and tools
RUN apt-get update && apt-get install -y \
    gcc \
    libglib2.0-0 \
    libgl1-mesa-glx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install numpy==1.26.4
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the main script
CMD ["python", "main.py"]
