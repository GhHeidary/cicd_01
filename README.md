![Tests](https://github.com/GhHeidary/cicd_01/actions/workflows/test.yml/badge.svg)
# 🧮 CI/CD Übung – Rechner

Ein einfaches Python-Projekt zum Lernen von **CI/CD mit GitHub Actions**.

## ✨ Features

- ➕ Grundrechenarten (addieren, subtrahieren, multiplizieren, dividieren)
- 🔢 Potenz-Funktion
- 🧪 Automatische Tests mit pytest
- 🤖 CI/CD mit GitHub Actions
- 🎯 Matrix-Build (Python 3.9, 3.10, 3.11)

## 🚀 Installation

```bash
git clone git@github.com:GhHeidary/cicd_01.git
cd cicd_01
pip install pytest
```

## 💻 Nutzung

```python
from rechner import addiere, potenz

print(addiere(2, 3))   # 5
print(potenz(2, 3))    # 8
```

## 🧪 Tests ausführen

```bash
pytest test_rechner.py -v
```

## 📚 Über dieses Projekt

Erstellt im Rahmen des **MLOps-Kurses** am IfaDW.
Modul 4: Pipelines & CI/CD.

## 📜 Lizenz

MIT