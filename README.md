# 💱 Currency Converter CLI

A simple command-line tool to convert between world currencies using live exchange rates from the [open.er-api.com](https://open.er-api.com) API.

---

## 🚀 Features

- Convert from one currency to another
- Get real-time exchange rates
- List all available currency codes
- Error handling for invalid inputs

---

## 🧠 How to Use

### 🔧 Install dependencies:

```bash
pip install -r requirements.txt
```
### 🔁 Run a conversion:
```bash
python main.py --amount 100 --from_currency USD --to_currency INR
```
### 🧾 List supported currencies:
```bash
python main.py --list
```
### 🛠️ Example Output
```bash
100 USD = 8325.00 INR
✅ Available currencies:
AUD, CAD, CHF, EUR, GBP, INR, JPY, USD, ...
```
### 📦 Tech Stack
    •	Python 3.10+
    •	requests
    •	argparse
### 📂 Folder Structure
	•	main.py – CLI entrypoint
	•	currency.py – core conversion logic
	•	requirements.txt – dependency list
### 🔒 License
    MIT – do whatever you want.