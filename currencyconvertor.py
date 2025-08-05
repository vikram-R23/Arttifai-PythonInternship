import requests

# Open API that doesn't need a key
BASE_URL = "https://open.er-api.com/v6/latest/"

def convert_currency(amount, from_currency, to_currency):
    try:
        from_currency = from_currency.upper().replace('"', '').strip()
        to_currency = to_currency.upper().replace('"', '').strip()

        response = requests.get(BASE_URL + from_currency)
        data = response.json()

        if data.get("result") != "success":
            print("API Error:", data.get("error-type", "Unknown error"))
            return

        rates = data.get("rates")
        if not rates or to_currency not in rates:
            print(f"Invalid target currency: {to_currency}")
            return

        converted = amount * rates[to_currency]
        print(f"\nConverted Amount: {converted:.2f} {to_currency}")

    except Exception as e:
        print("Unexpected error:", e)

# Input section
try:
    amt = float(input("Enter amount: "))
    src = input("Convert from (e.g., USD): ")
    tgt = input("Convert to (e.g., INR): ")

    convert_currency(amt, src, tgt)

except ValueError:
    print("Invalid amount. Please enter a number.")