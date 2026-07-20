# Hash a collected file for integrity verification
sha256sum collected_evidence.html
# Output: a4f8e2c... collected_evidence.html

# Create a timestamped collection log entry
echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') | Source: LinkedIn | Query: 'John Doe Portland OR' | Results: 3 profiles found | Screenshots: screenshots/linkedin_001-003.png" >> collection_log.txt
