from static import Currency
import datetime
import requests

class CurrencyConverter():
    api_key:str
    exchange_rate_cache: dict[tuple[Currency, Currency], float]
    def __init__(self):
        file = open("api_key.txt", "r")
        self.api_key = file.read()

    def convert_amount(self, amount:float, from_currency:Currency, to_currency:Currency, date: datetime.date):
        requests.get(f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD")
        pass


    def fetch_exchange_rate(self):
        pass

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()


