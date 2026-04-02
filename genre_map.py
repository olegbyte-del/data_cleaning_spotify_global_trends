genre_map = {
    "Pop": ["Pop", "K-Pop", "Alternative Pop", "Synth-Pop", "Indie Pop", "Folk Pop", "Dance-Pop"],
    "Rock": ["Rock", "Alternative Rock", "Indie Rock", "Psychedelic Rock", "Hard Rock", "Nu Metal", "Grunge", "Britpop", "Swamp Rock", "New Wave"],
    "Hip Hop": ["Hip Hop", "Rap", "Trap"],
    "R&B": ["R&B", "Contemporary R&B", "Soul", "Pop Soul"],
    "Latin": ["Reggaeton", "Regional Mexicano", "Regional Mexican", "Latin", "Dancehall"],
    "Electronic": ["Electronic", "Dance", "Dance-Pop"],
    "Uncategorized": ["Billboard Hot 100", "Toronto", "Soundtrack", "Special Purpose Artist", "Dolby Atmos"],
}

def subgenre_to_main_genre(subgenre: str) -> str:
    for main_genre, subgenres in genre_map.items():
        if subgenre in subgenres:
            return main_genre
    return subgenre