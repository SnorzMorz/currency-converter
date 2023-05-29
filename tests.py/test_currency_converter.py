def test_convert_amount():
    currency_converter = CurrencyConverter()
    print(currency_converter.convert_amount(100, Currency.EUR, Currency.USD))