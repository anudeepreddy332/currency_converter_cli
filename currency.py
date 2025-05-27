import os.path
import pandas as pd
from datetime import datetime as dt
import requests
from tabulate import tabulate

class Currency:
    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency

    def get_exchange_rate(self):
        try:
            url = f"https://open.er-api.com/v6/latest/{self.from_currency.upper()}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException:
            print("[ERROR] Network problem. Please check your internet.")
            return None

        if "rates" not in data:
            print("[ERROR] Malformed response from API.")
            return None

        rate = data["rates"].get(self.to_currency.upper())
        if not rate:
            print(f"[ERROR] Invalid 'to_currency': {self.to_currency}")
            return None

        return rate

    def convert(self):
        if self.amount <= 0:
            print("[ERROR] Amount must be greater than zero.")
            return None

        rate = self.get_exchange_rate()
        if rate is None:
            return None

        result = self.amount * rate
        self.log_to_csv(rate, result)
        return result

    def log_to_csv(self, rate, result):

        log_entry = {
            "Timestamp": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Amount": self.amount,
            "From": self.from_currency,
            "To": self.to_currency,
            "Rate": round(rate,4),
            "Converted": round(result,2)
        }
        file_path = "history.csv"
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([log_entry])

        df.to_csv(file_path, index=False)

    def show_history(self,limit=10):
        try:
            df = pd.read_csv("history.csv")
            df = df.tail(limit)
            print("\n📋 Conversion History (Last {}):\n".format(limit))
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
        except FileNotFoundError:
            print("⚠️ No history found.")

    @staticmethod
    def list_currencies():
        try:
            url = "https://open.er-api.com/v6/latest/USD"
            response = requests.get(url)
            response.raise_for_status()
            my_data = response.json()
            currency_list = sorted(my_data["rates"].keys())
            print("✅ Available currencies:")
            print(", ".join(currency_list))

            return currency_list
        except requests.exceptions.RequestException:
            print("[ERROR] Network problem. Please check your internet.")
            return None