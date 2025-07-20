import os
import json

BIBLES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bibles")
loaded_bibles = {}

def load_bible(version):
    """Load the specified Bible version from JSON, caching it for future use."""
    if version in loaded_bibles:
        return loaded_bibles[version]
    path = os.path.join(BIBLES_DIR, f"{version}.json")
    with open(path, encoding="utf-8") as f:
        bible = json.load(f)
        loaded_bibles[version] = bible
        return bible

def get_book_map():
    return {
        "gen": "Genesis",
        "ex": "Exodus",
        "lev": "Leviticus",
        "num": "Numbers",
        "deut": "Deuteronomy",
        "jos": "Joshua",
        "jdg": "Judges",
        "rut": "Ruth",
        "1sa": "1 Samuel", "1sam": "1 Samuel",
        "2sa": "2 Samuel", "2sam": "2 Samuel",
        "1ki": "1 Kings", "2ki": "2 Kings",
        "ps": "Psalm", "psa": "Psalm",
        "pro": "Proverbs",
        "ecc": "Ecclesiastes",
        "sos": "Song of Solomon",
        "isa": "Isaiah",
        "jer": "Jeremiah",
        "lam": "Lamentations",
        "eze": "Ezekiel",
        "dan": "Daniel",
        "hos": "Hosea",
        "joe": "Joel",
        "amo": "Amos",
        "oba": "Obadiah",
        "jon": "Jonah",
        "mic": "Micah",
        "nah": "Nahum",
        "hab": "Habakkuk",
        "zep": "Zephaniah",
        "hag": "Haggai",
        "zec": "Zechariah",
        "mal": "Malachi",
        "mat": "Matthew", "mt": "Matthew",
        "mrk": "Mark", "mk": "Mark",
        "luk": "Luke", "lk": "Luke",
        "jn": "John",
        "act": "Acts",
        "rom": "Romans",
        "1co": "1 Corinthians",
        "2co": "2 Corinthians",
        "gal": "Galatians",
        "eph": "Ephesians",
        "phi": "Philippians",
        "col": "Colossians",
        "1th": "1 Thessalonians",
        "2th": "2 Thessalonians",
        "1ti": "1 Timothy",
        "2ti": "2 Timothy",
        "tit": "Titus",
        "phm": "Philemon",
        "heb": "Hebrews",
        "jam": "James",
        "1pe": "1 Peter",
        "2pe": "2 Peter",
        "1jn": "1 John",
        "2jn": "2 John",
        "3jn": "3 John",
        "jud": "Jude",
        "rev": "Revelation"
    }

book_map = get_book_map()

def get_version_map():
    return {
        "nasb": "NASB",
        "niv": "NIV",
        "nasb95": "NASB1995",
        "esv": "ESV",
        "nkjv": "NKJV",
        "web": "WEB",
        "tel": "TeluguBSI",
        "et": "NASB_TeluguBSI"
    }

version_map = get_version_map()
