<p align="Center" style="font-size:40px; font-weight:bold; letter-spacing:4px;">Easy Verse</p>
<p align="Center" style="font-size:15px;"><em>Bible search plugin for Flow Launcher</em><p>


# EasyVerse
*Bible Search Plugin for Flow Launcher*

EasyVerse is a powerful and user-friendly Bible search plugin for [Flow Launcher](https://www.flowlauncher.com/). It allows you to quickly look up Bible verses, search by keyword, and compare across multiple versions—all from your keyboard.

---

## Features

- 🔍 **Quick verse lookup** by reference (e.g., `jn 3 16` or `gen 1:1`)
- 🗝️ **Keyword search** across the whole Bible, a specific book, or a chapter (e.g., `find love`, `find faith jn`, `find hope rom 8`)
- 📖 **Multiple versions supported**: NASB, ESV, NKJV, WEB, TeluguBSI, and more
- 🏷️ **Book abbreviations and aliases** (e.g., `jn` for John, `1co` for 1 Corinthians)
- 📝 **Set your default version** (e.g., `setversion esv`)
- 📋 **Copy full verse and reference** to clipboard with one press
- 🧠 **Graceful error messages and suggestions** for typos
- ⚡ **Fast, modular, and extensible codebase**

---

## Installation

1. **Download or clone** this repository into your Flow Launcher plugins directory:
   - `C:/Users/<YourUser>/AppData/Roaming/FlowLauncher/Plugins/EasyVerse`
2. Ensure the following structure:
   ```
   EasyVerse/
     main.py
     plugin.json
     settings.json (auto-created)
     Images/
     bibles/
     easyverse/
       __init__.py (optional)
       bible.py
       settings.py
       parsing.py
       keyword.py
   ```
3. **Restart Flow Launcher**. The plugin should appear in the Plugins list.
4. **Python 3.7+ required**. Set the correct Python path in Flow Launcher settings if needed.

---

## Usage

### **Verse Lookup**
- `verse jn 3 16`
- `verse gen 1:1`
- `verse 1co 13 4 esv`

### **Keyword Search**
- `verse find love`
- `verse find faith jn`
- `verse find hope rom 8 nkjv`

### **Set Default Version**
- `verse setversion esv`
- All future queries will use ESV unless you specify another version.

### **Book/Chapter Suggestions**
- Type only a book (e.g., `verse jn`) to see available chapters.
- Type a book and chapter (e.g., `verse jn 3`) to see available verses.

### **Error Handling**
- If you mistype a book, EasyVerse will suggest the closest matches.
- If a verse is not found, you'll get a helpful message.

---

## Configuration

- **Default version** is stored in `settings.json` in the plugin folder.
- Supported versions: `nasb`, `nasb95`, `esv`, `nkjv`, `web`, `tel` (TeluguBSI)
- To add more versions, place the corresponding JSON file in the `bibles/` folder and update `bible.py` if needed.

---

## Development & Contribution

- The codebase is modular and easy to extend.
- Main logic is in `main.py`, with supporting modules in `easyverse/`.
- PRs and suggestions are welcome!
- For bug reports, please include your Flow Launcher version, OS, and a description of the issue.

---

## Credits

- Bible data files are not included; please use your own or open-source versions.
- Inspired by the Flow Launcher and open-source Bible tools community.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
