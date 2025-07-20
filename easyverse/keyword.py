from .bible import load_bible, book_map, version_map

def search_keyword(keyword, version, book_key=None, chapter=None):
    """
    Search for a keyword in the specified Bible version.
    Optionally filter by book and/or chapter.
    Returns a list of (reference, verse_text) tuples.
    """
    keyword = keyword.lower()
    bible = load_bible(version)
    results = []
    books_to_search = [book_map.get(book_key, book_key.title())] if book_key else bible.keys()
    for book in books_to_search:
        if book not in bible:
            continue
        chapters_to_search = [str(chapter)] if chapter else bible[book].keys()
        for ch in chapters_to_search:
            if ch not in bible[book]:
                continue
            for verse in bible[book][ch]:
                text = bible[book][ch][verse]
                if keyword in text.lower():
                    reference = f"{book} {ch}:{verse}"
                    results.append((reference, text))
    return results