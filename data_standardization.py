import numpy as np
import pandas as pd

genre_map = {
    "Pop": ["Pop", "K-Pop", "Alternative Pop", "Synth-Pop", "Indie Pop", "Folk Pop", "Dance-Pop"],
    "Rock": ["Rock", "Alternative Rock", "Indie Rock", "Psychedelic Rock", "Hard Rock", "Nu Metal", "Grunge", "Britpop", "Swamp Rock", "New Wave"],
    "Hip Hop": ["Hip Hop", "Rap", "Trap"],
    "R&B": ["R&B", "Contemporary R&B", "Soul", "Pop Soul"],
    "Latin": ["Reggaeton", "Regional Mexicano", "Regional Mexican", "Latin", "Dancehall"],
    "Electronic": ["Electronic", "Dance", "Dance-Pop"],
    "Uncategorized": ["Billboard Hot 100", "Toronto", "Soundtrack", "Special Purpose Artist", "Dolby Atmos"],
}

fullname_country = {
    "US": "United States",
    "KR": "South Korea",
    "GB": "United Kingdom",
    "PR": "Puerto Rico",
    "SE": "Sweden",
    "AU": "Australia",
    "JM": "Jamaica",
    "IT": "Italy",
    "CA": "Canada",
    "MX": "Mexico",
    "CO": "Colombia",
    "JP": "Japan",
    "FR": "France",
    "IE": "Ireland",
    "NO": "Norway",
}

# country domain --> fullname country
def country_domain_to_fullname_country(domain_name: str) -> str:
    for domain, country in country_domain_to_fullname_country.items():
        if domain == domain_name:
            return country
    return domain

# days is based on longevity
def categorize_longevity(days):
    if pd.isna(days):
        return 'Unknown'
    elif days <= 30:
        return 'New'
    elif days <= 100:
        return 'Stable Hit'
    else:
        return 'Evergreen'

# popularity is based on streams
def categorize_popularity(streams):
    if pd.isna(streams):
        return 'Unknown'
    elif streams >= 5_000_000:
        return 'Viral'
    elif streams >= 3_000_000:
        return 'Trending'
    elif streams >= 1_500_000:
        return 'Stable'
    else:
        return 'Declining'
    
def subgenre_to_main_genre(subgenre: str) -> str:
    for main_genre, subgenres in genre_map.items():
        if subgenre in subgenres:
            return main_genre
    return subgenre