# SpiderFoot - Automated OSINT reconnaissance
docker pull spiderfoot/spiderfoot
docker run -p 5001:5001 spiderfoot/spiderfoot

# theHarvester - Email, subdomain, and name harvester
docker pull kalilinux/kali-rolling
docker run -it kalilinux/kali-rolling bash -c \
    "apt update && apt install -y theharvester && theharvester"

# Maltego (requires X11 forwarding for GUI)
# Best run in a VM rather than container for GUI tools

# Sherlock - Username search across social networks
docker run -it --rm python:3.11-slim bash -c \
    "pip install sherlock-project && sherlock username"

# Amass - Network mapping and attack surface discovery
docker pull caffix/amass
docker run -v ~/amass-output:/output caffix/amass enum \
    -d target.com -dir /output

# Photon - Web crawler designed for OSINT
docker run -it --rm python:3.11-slim bash -c \
    "pip install photon && photon -u https://target.com"

# Recon-ng - Full-featured reconnaissance framework
docker run -it --rm python:3.11-slim bash -c \
    "pip install recon-ng && recon-ng"
