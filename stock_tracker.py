import requests

API_KEY = "your_api_key"
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_price(symbol):
    params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    print(f"Stock Price for {symbol}: ${data['Global Quote']['05. price']}")

symbol = input("Enter stock symbol: ")
get_stock_price(symbol)
