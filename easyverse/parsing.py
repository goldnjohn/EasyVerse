import re
from .bible import book_map, version_map

def parse_query(query):
    query = query.strip()
    version_key = None
    version_match = re.search(r"\s(\w+)$", query)
    if version_match:
        possible_version = version_match.group(1)
        if possible_version.lower() in [v.lower() for v in version_map.keys()]:
            version_key = possible_version
            query = query[:version_match.start()].strip()
    match = re.match(r"^([1-3]?\s?[a-zA-Z]+)\s*(\d+)[:\s]+(\d+)$", query)
    if not match:
        match = re.match(r"^([1-3]?[a-zA-Z]+)(\d+)[:\s]+(\d+)$", query)
    if match:
        book_key, chapter, verse = match.groups()
        return book_key.strip().replace(' ', '').lower(), chapter, verse, version_key or None
    parts = query.lower().split()
    if len(parts) < 3:
        return None, None, None, None
    book_key, chapter, verse = parts[0], parts[1], parts[2]
    version_key = parts[3] if len(parts) >= 4 else version_key or None
    return book_key, chapter, verse, version_key

def get_book_name(book_key, book_map):
    if not book_key:
        return ""
    return book_map.get(book_key, book_key.title())
