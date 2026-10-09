# Currency Converter

print("Currency Converter")
print("Available currencies: USD, INR, EUR, GBP")

# Input from user
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency: ").upper()
to_currency = input("Enter the target currency: ").upper()

# Exchange rates (relative to USD)
rates = {
    "USD": 1.0,
    "INR": 87.0,
    "EUR": 0.92,
    "GBP": 0.79
}

# Check if currencies are valid
if from_currency in rates and to_currency in rates:
    # Convert source currency to USD, then USD to target currency
    usd_amount = amount / rates[from_currency]
    converted_amount = usd_amount * rates[to_currency]

    print(f"\n{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("Invalid currency code! Please use USD, INR, EUR, or GBP.")