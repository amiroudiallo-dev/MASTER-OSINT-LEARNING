# Passive DNS lookup
dig +short target-domain.com
dig +short -x 192.168.1.1

# WHOIS lookup
whois target-domain.com

# Certificate Transparency log search
curl -s "https://crt.sh/?q=%.target-domain.com&output=json" | \
     jq '.[] | {name_value, not_before, not_after}'

# Shodan CLI query
shodan search "hostname:target-domain.com"
