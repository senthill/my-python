#!/usr/bin/env python3

""" A simple calculator module """
import urllib.request
import json

# x = float(input("WHat's x? "))
# y = float(input("WHat's y? "))

# z = round(x + y)

# print(f"{z:,}")


# z = x/y
# print(f"{z}")

def hello():
    print("Hello, World!")

def multiply(a, b):
    return a * b

# Write a function to do a currency conversion using an exchange rate from online API
def convert_currency(amount, from_currency, to_currency):
    """
    Converts amount from one currency to another using a free API.
    Example: convert_currency(100, 'USD', 'EUR')
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            rates = data.get('rates')
            if not rates or to_currency.upper() not in rates:
                print(f"Error: Currency {to_currency} not found.")
                return None
            rate = rates[to_currency.upper()]
            return amount * rate
    except Exception as e:
        print(f"Error converting currency: {e}")
        return None

hello()

# Test cases
print("-" * 20)
print("Testing Currency Conversion:")
sgd_amount = 10
inr_from_sgd = convert_currency(sgd_amount, 'SGD', 'INR')
if inr_from_sgd is not None:
    print(f"{sgd_amount} SGD is {inr_from_sgd:.2f} INR")

usd_amount = 10
inr_from_usd = convert_currency(usd_amount, 'USD', 'INR')
if inr_from_usd is not None:
    print(f"{usd_amount} USD is {inr_from_usd:.2f} INR")
print("-" * 20)