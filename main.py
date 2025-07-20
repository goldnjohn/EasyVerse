import sys
import os
import json
import difflib

# Ensure the plugin root is in sys.path for easyverse imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from easyverse.bible import load_bible, book_map, version_map
from easyverse.settings import load_settings, save_settings
from easyverse.parsing import parse_query, get_book_name
from easyverse.keyword import search_keyword

settings = load_settings()

def build_result(book, chapter, verse, version, verse_text):
    """Format a result for Flow Launcher."""
    reference_and_verse = f"{book} {chapter}:{verse} ({version}): {verse_text}"
    return {
        "Title": f"{book} {chapter}:{verse} ({version})",
        "SubTitle": verse_text,
        "IcoPath": "Images/easyverse.png",
        "JsonRPCAction": {
            "method": "Flow.Launcher.Plugin.CopyToClipboard",
            "parameters": [reference_and_verse],
            "dontHideAfterAction": False
        }
    }

def build_error_result(message):
    """Format an error result for Flow Launcher."""
    return {
        "Title": "Verse not found",
        "SubTitle": message,
        "IcoPath": "Images/easyverse.png"
    }

def search(query):
    """Main search logic: parse query, look up verse, and build results."""
    results = []
    # Keyword search: find <keyword> [book] [chapter] [version]
    if query.lower().startswith("find "):
        parts = query[5:].strip().split()
        # Check for version at the end
        version_key = None
        if parts and parts[-1].lower() in version_map:
            version_key = parts.pop(-1).lower()
        else:
            version_key = settings.get("default_version", "esv")
        # Try to parse book and chapter at the end
        book_key = chapter = None
        if len(parts) >= 2 and parts[-2].isalpha() and parts[-1].isdigit():
            book_key = parts[-2]
            chapter = parts[-1]
            keyword = " ".join(parts[:-2])
        elif len(parts) >= 1 and parts[-1].isalpha():
            book_key = parts[-1]
            keyword = " ".join(parts[:-1])
        else:
            keyword = " ".join(parts)
        version = version_map.get(version_key.lower(), "esv")
        matches = search_keyword(keyword, version, book_key, chapter)
        if not matches:
            return [{"Title": "No matches found", "SubTitle": f"No verses found for '{keyword}'."}]
        for ref, text in matches[:20]:  # Limit to 20 results
            results.append({
                "Title": ref + f" ({version})",
                "SubTitle": text,
                "IcoPath": "Images/easyverse.png",
                "JsonRPCAction": {
                    "method": "Flow.Launcher.Plugin.CopyToClipboard",
                    "parameters": [f"{ref} ({version}): {text}"],
                    "dontHideAfterAction": False
                }
            })
        return results
    # Handle setversion command
    if query.lower().startswith("setversion "):
        new_version = query.split()[1].lower()
        if new_version in version_map:
            settings["default_version"] = new_version
            save_settings(settings)
            return [{
                "Title": f"Default version set to {version_map[new_version]}",
                "SubTitle": f"All queries will now use {version_map[new_version]} unless you specify another version.",
                "IcoPath": "Images/easyverse.png"
            }]
        else:
            return [{
                "Title": f"Version '{new_version}' not recognized.",
                "SubTitle": f"Available versions: {', '.join(version_map.keys())}",
                "IcoPath": "Images/easyverse.png"
            }]
    book_key, chapter, verse, version_key = parse_query(query)
    if not book_key:
        return [{
            "Title": "Type: book chapter verse [version]",
            "SubTitle": "Example: jn 3 16 nkjv",
            "IcoPath": "Images/easyverse.png"
        }]
    # Use user default version if not specified
    version_key = version_key or settings.get("default_version", "esv")
    version = version_map.get(version_key.lower(), "ESV")
    book = get_book_name(book_key, book_map)
    try:
        bible = load_bible(version)
        # Only book provided
        if book_key and not chapter and not verse:
            if book in bible:
                chapters = list(bible[book].keys())
                for ch in chapters:
                    results.append({
                        "Title": f"{book} {ch}",
                        "SubTitle": f"Show verses in {book} chapter {ch}",
                        "IcoPath": "Images/easyverse.png"
                    })
                return results
        # Book and chapter provided
        if book_key and chapter and not verse:
            if book in bible and chapter in bible[book]:
                verses = list(bible[book][chapter].keys())
                for v in verses:
                    results.append({
                        "Title": f"{book} {chapter}:{v}",
                        "SubTitle": f"Show verse {v} in {book} chapter {chapter}",
                        "IcoPath": "Images/easyverse.png"
                    })
                return results
        # Book, chapter, and verse provided (normal lookup)
        if book not in bible:
            book_str = book or ""
            close_books = difflib.get_close_matches(book_str, list(bible.keys()), n=3, cutoff=0.5)
            if not close_books:
                close_books = [b for b in bible.keys() if b.lower().startswith(book_str.lower())]
            if not close_books and book_str:
                close_books = [b for b in bible.keys() if book_str.lower() in b.lower()]
            suggestion = f"Book '{book_str}' not found. Did you mean: {', '.join(close_books) if close_books else 'No suggestions'}?"
            results.append(build_error_result(suggestion))
            return results
        verse_text = bible[book][chapter][verse]
        results.append(build_result(book, chapter, verse, version, verse_text))
    except Exception as e:
        results.append(build_error_result(f"Check book, chapter, verse, or version. ({str(e)})"))
    return results

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            try:
                arg = json.loads(sys.argv[1])
                query = arg.get("parameters", [""])[0]
            except Exception:
                query = sys.argv[1]
        else:
            query = ""
        results = search(query)
        print(json.dumps({"result": results}))
    except Exception as e:
        print(json.dumps({
            "result": [{
                "Title": "Plugin Error",
                "SubTitle": str(e),
                "IcoPath": "Images/easyverse.png"
            }]
        }))