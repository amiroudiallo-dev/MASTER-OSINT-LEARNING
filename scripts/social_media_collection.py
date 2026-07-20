# Using Twint (or successor tools) for Twitter/X collection
twint -u targetuser --since 2025-01-01 -o output.json --json

# Gallery-dl for social media image archiving
gallery-dl https://www.instagram.com/targetuser/

# yt-dlp for video archiving
yt-dlp --write-info-json --write-thumbnail \
        --write-description --write-annotations \
        "https://www.youtube.com/watch?v=VIDEOID"
