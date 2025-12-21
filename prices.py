import yfinance as yf


def get_stock_price(symbol: str) -> float:
    stock = yf.Ticker(symbol)
    print("Stock object: ", stock)
    # Get current market price
    current_price = stock.info["currentPrice"]
    print("Current price:", current_price)
    return current_price

# Example usage
stock = input("Stock of interest:")
get_stock_price(stock.upper())