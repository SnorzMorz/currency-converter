from static import Currency
import datetime
import requests

class CurrencyConverter():
    api_key:str
    exchange_rate_cache: dict[tuple[Currency, Currency], float]

    def __init__(self):
        file = open("api_key.txt", "r")
        self.api_key = file.read()
        self.exchange_rate_cache = []

    def convert_amount(self, amount:float, from_currency:Currency, to_currency:Currency)-> float:
        if (from_currency, to_currency) in self.exchange_rate_cache:
            return amount * self.exchange_rate_cache[(from_currency, to_currency)]
        
        response: dict = requests.get(f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_currency.name}/{to_currency.name}/{amount}").json()

        if response["result"] != "success":
            raise Exception(response["error-type"])
        return response["conversion_result"]
    
    def convert_amount_historic(self, amount:float, from_currency:Currency, to_currency:Currency)-> float:
        if (from_currency, to_currency) in self.exchange_rate_cache:
            return amount * self.exchange_rate_cache[(from_currency, to_currency)]
        
        response: dict = requests.get(f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_currency.name}/{to_currency.name}/{amount}").json()

        # GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/history/USD/YEAR/MONTH/DAY

        if response["result"] != "success":
            raise Exception(response["error-type"])
        return response["conversion_result"]


    def fetch_exchange_rate(self):
        pass

def main():
    print("Hello World!")

if __name__ == "__main__":
    currency_converter = CurrencyConverter()
    print(currency_converter.convert_amount(100, Currency.EUR, Currency.USD))


