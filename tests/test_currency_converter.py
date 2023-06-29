import datetime

import pytest
from main import CurrencyConverter
from static import Currency

def test_convert_amount():
    currency_converter = CurrencyConverter()
    assert currency_converter.convert_amount(100, Currency.EUR, Currency.USD) == 109.21

def test_convert_amount_same_currency():
    currency_converter = CurrencyConverter()
    assert currency_converter.convert_amount(100, Currency.EUR, Currency.EUR) == 100.00

pytest.mark.skip("Plan upgrade required")
def test_convert_amount_historic():
    currency_converter = CurrencyConverter()
    assert currency_converter.convert_amount_historic(100, Currency.EUR, Currency.EUR, datetime.datetime(2020, 1, 1)) == 100.00