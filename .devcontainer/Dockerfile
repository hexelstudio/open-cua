# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install additional packages if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Do NOT switch to a non-root user; remain as root
# USER vscode

# (Optional) Add any additional root-specific commands below
