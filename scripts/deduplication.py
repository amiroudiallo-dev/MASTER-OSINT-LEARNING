#Lors de la collecte à partir de plusieurs sources, il est inévitable de dupliquer des données.
#La déduplication garantit que chaque point de données n’est compté qu’une seule fois. 

# Simple deduplication of collected social media profiles
profiles = [
    {"platform": "twitter", "username": "johndoe", "url": "..."},
    {"platform": "twitter", "username": "johndoe", "url": "..."},  # duplicate
    {"platform": "linkedin", "username": "john-doe-123", "url": "..."},
]

unique_profiles = {f"{p['platform']}:{p['username']}": p
                   for p in profiles}
