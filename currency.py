import requests

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
        return result

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