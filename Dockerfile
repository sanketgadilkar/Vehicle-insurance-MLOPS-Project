FROM python:3.11-slim-buster

WORKDIR /app

# Install system dependencies (recommended)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Ensure templates & static exist
RUN mkdir -p templates static

EXPOSE 5000

# ✅ Correct way to start FastAPI in Docker
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
