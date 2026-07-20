# Example: Normalizing dates from different sources
from dateutil import parser

raw_dates = [
    "March 15, 2025",      # News article format
    "2025-03-15",           # ISO format
    "15/03/2025",           # European format
    "03/15/2025",           # US format
    "1710460800",           # Unix timestamp
]

normalized = []
for date_str in raw_dates:
    try:
        if date_str.isdigit():
            dt = datetime.fromtimestamp(int(date_str))
        else:
            dt = parser.parse(date_str)
        normalized.append(dt.strftime("%Y-%m-%d"))
    except Exception as e:
        normalized.append(f"PARSE_ERROR: {date_str}")
