FROM python:3.12-slim

# Avoid buffering issues and unnecessary .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace