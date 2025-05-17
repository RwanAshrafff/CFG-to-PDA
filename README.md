# 🎯 CFG to PDA Converter

A tool that converts **Context-Free Grammar (CFG)** to a **Pushdown Automaton (PDA)** with visualization and string testing capabilities.

## 🗂 Project Structure

CFG-to-PDA-Converter/
│
├── src/
│ ├── app.py # Flask web interface
│ ├── grammar.py # CFG parser
│ ├── pda.py # PDA construction & visualization
│ ├── cli.py # Command-line interface
├── templates/ # Web UI templates
└── README.md

## 🔥 Features
- ✅ Parses CFG with  `->` notation
- ✅ Visualizes PDA transitions using Graphviz
- ✅ Tests string acceptance
- ✅ Web and CLI interfaces

## ⚙ Installation
```bash
pip install flask graphviz
brew install graphviz  # OR sudo apt-get install graphviz
