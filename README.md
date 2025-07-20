![demo](/Images/demo.gif)

<img alt="logo" align="right" src="./Images/easyverse.png" width="100" height="100">

<p align="left" style="font-size:40px; font-weight:bold; letter-spacing:3px;">Easy Verse</p>
<p align="left" style="font-size:15px;"><em>Bible search plugin for Flow Launcher</em><p>

<br>
<br>
<br>

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
2. **Restart Flow Launcher**. The plugin should appear in the Plugins list.
3. **Python 3.7+ required**. Set the correct Python path in Flow Launcher settings if needed.

---

## Usage

### **Verse Lookup**
- `ver jn 3 16`
- `ver gen 1:1`
- `ver 1co 13 4 esv`

### **Keyword Search**
- `ver find love`
- `ver find faith jn`
- `ver find hope rom 8 nkjv`

### **Set Default Version**
- `ver setversion esv`
- All future queries will use ESV unless you specify another version.

### **Book/Chapter Suggestions**
- Type only a book (e.g., `ver jn`) to see available chapters.
- Type a book and chapter (e.g., `ver jn 3`) to see available verses.

### **Error Handling**
- If you mistype a book, EasyVerse will suggest the closest matches.
- If a verse is not found, you'll get a helpful message.

---

## Configuration

- **Default version** is stored in `settings.json` in the plugin folder.
- Supported versions: `nasb`, `nasb95`, `esv`, `nkjv`, `web`, `tel` (TeluguBSI)
- To add more versions, place the corresponding JSON file in the `bibles/` folder and update `bible.py` if needed.

---

## Credits

- Inspired by the Flow Launcher and open-source Bible tools community.
