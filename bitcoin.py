# This is a Python script that retrieves the current price of Bitcoin in USD from the Coindesk API and
# calculates the cost of a specified number of Bitcoins. The script takes a command line argument for
# the number of Bitcoins and uses the `requests` library to make an HTTP GET request to the API. It
# then parses the JSON response to extract the Bitcoin price and calculates the cost based on the
# specified number of Bitcoins. Finally, it formats the cost as a string and prints it to the console.
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py <number of bitcoins>")

try:
    num_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Error: Number of bitcoins must be a decimal")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    bitcoin_price = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Error: Failed to retrieve Bitcoin price")

cost = num_bitcoins * bitcoin_price
formatted_cost = "{:,.4f}".format(cost)

print(f"The current cost of {num_bitcoins} Bitcoins is ${formatted_cost} USD")