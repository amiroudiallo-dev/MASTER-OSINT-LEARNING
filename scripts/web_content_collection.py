# Archiving a webpage with wget (preserving structure)
wget --mirror --convert-links --adjust-extension \
     --page-requisites --no-parent \
     --user-agent="Mozilla/5.0" \
     https://target-website.com/

# Using HTTrack for full site mirroring
httrack "https://target-website.com/" \
        -O "/investigations/case-001/website-mirror" \
        --depth=3

# Capturing a single page with SingleFile (CLI)
single-file https://target-website.com/page \
            --output /investigations/case-001/page.html
