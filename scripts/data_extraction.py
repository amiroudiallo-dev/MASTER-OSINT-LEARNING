# Extracting email addresses from collected web pages
import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return list(set(re.findall(pattern, text)))

# Extracting phone numbers
def extract_phones(text):
    pattern = r'[\+]?[(]?[0-9]{1,4}[)]?[-\s\./0-9]{7,15}'
    return list(set(re.findall(pattern, text)))

# Extracting EXIF data from images
# Using exiftool
# exiftool -json collected_image.jpg
