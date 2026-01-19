import yfinance as yf

def get_forward_pe(ticker_symbol):
    stock = yf.Ticker(ticker_symbol.upper())
    info = stock.info
    return info.get("forwardPE")

ticker = input("Enter a stock ticker symbol: ")
forward_pe = get_forward_pe(ticker)

if forward_pe is not None:
    print(f"{ticker.upper()} Forward P/E Ratio: {forward_pe}")
else:
    print("Forward P/E data not available.")
