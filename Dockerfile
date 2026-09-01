# Start from the official lightweight Python image, 3.14 unless overridden
ARG PYTHON_VERSION=3.14
FROM python:${PYTHON_VERSION}-slim

# No .pyc files, and don't buffer the logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list first (helps Docker cache dependencies)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py .

# Don't run as root
RUN useradd --create-home --uid 10001 appuser
USER appuser

# Tell Docker that this container will listen on port 8080
EXPOSE 8080

# Start the Flask app
CMD ["python", "app.py"]
