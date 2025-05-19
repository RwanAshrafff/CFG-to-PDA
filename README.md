# 🎯 CFG to PDA Converter

A tool that converts **Context-Free Grammar (CFG)** to a **Pushdown Automaton (PDA)** with visualization and string testing capabilities.

## 🗂 Project Structure
```
CFG-to-PDA/
├── src/
│   ├── static/        # Static files for the Flask app (e.g., CSS, JS)
│   ├── templates/     # HTML templates for rendering pages
│   ├── app.py         # Main Flask application entry point
│   ├── grammer.py     # Logic for parsing CFG
│   ├── pda.py         # Logic for generating the PDA from the CFG
├── README.md

```
---
## 🔥 Features
- ✅ Parses CFG with  `->` notation
- ✅ Visualizes PDA transitions using Graphviz
- ✅ Tests string acceptance
- ✅ Web and CLI interfaces

## ⚙ How to Run the Web App

### 1. 📦 Install Python Packages

Make sure you have Python 3.7+ installed.

```bash
pip install flask graphviz
```
### 2. 🧱 Install Graphviz (System Package)

> Needed for rendering the visual graphs

- **Windows:** Download from https://graphviz.org/download/
- **Linux:** `sudo apt install graphviz`
- **macOS:** `brew install graphviz`

✅ Make sure the `bin/` directory is in your PATH (for dot executable).

---
### 3. 🚀 Run the Web App

```bash
cd src
python app.py
```

Then open:

```
http://127.0.0.1:5000
```
## 📜 License

MIT License ©

---
