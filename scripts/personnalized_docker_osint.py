# Dockerfile for custom OSINT toolkit
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Install base dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    git curl wget jq whois dnsutils \
    nmap nikto \
    tor torsocks \
    exiftool \
    chromium-browser \
    && rm -rf /var/lib/apt/lists/*

# Install Python OSINT tools
RUN pip3 install --no-cache-dir \
    shodan \
    censys \
    holehe \
    socialscan \
    maigret \
    twint \
    instaloader \
    waybackpy \
    recon-ng

# Install Sherlock
RUN pip3 install --no-cache-dir sherlock-project

# Install theHarvester
RUN pip3 install --no-cache-dir theHarvester

# Create working directory
RUN mkdir -p /osint/output
WORKDIR /osint

# Copy custom scripts
COPY scripts/ /osint/scripts/

# Default command
CMD ["/bin/bash"]
