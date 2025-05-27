# 💱 Currency Converter CLI

A simple command-line tool to convert between world currencies using live exchange rates from the [open.er-api.com](https://open.er-api.com) API.

---

## 🚀 Features

- Convert from one currency to another
- Get real-time exchange rates
- List all available currency codes
- Error handling for invalid inputs
- Automatically logs each conversion to a `history.csv` file
- View conversion history with the `--history` flag
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

### 📜 View conversion history:
```bash
python main.py --history
```

### 🛠️ Example Output
```bash
100 USD = 8325.00 INR
✅ Available currencies:
AUD, CAD, CHF, EUR, GBP, INR, JPY, USD, ...
```

### 🧾 History Example Output:

```
📋 Conversion History (Last 10):

╒═════════════════════╤══════════╤════════╤══════╤══════════╤═════════════╕
│ Timestamp           │   Amount │ From   │ To   │     Rate │   Converted │
╞═════════════════════╪══════════╪════════╪══════╪══════════╪═════════════╡
│ 2025-05-27 10:15:04 │      100 │ AUD    │ INR  │  55.2824 │     5528.24 │
╘═════════════════════╧══════════╧════════╧══════╧══════════╧═════════════╛
```
### 📦 Tech Stack
    •	Python 3.10+
    •	requests
    •	argparse
    •	pandas
    •	tabulate
### 📂 Folder Structure
	•	main.py – CLI entrypoint
	•	currency.py – core conversion logic
	•	requirements.txt – dependency list
### 🔒 License
    MIT – do whatever you want.