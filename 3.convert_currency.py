"""importing currency_converter module """
from currency_converter import CurrencyConverter

def currency_conver():
    """convertion function"""

    currency = CurrencyConverter()  #
    amount = int(input("Enter Amount :"))
    from_cur = input("Enter From Currency : ").upper()
    to_cur = input("Enter to Currency : ").upper()
    print(currency.convert(amount, from_cur, to_cur))


currency_conver()
