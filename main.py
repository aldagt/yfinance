from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/forward-pe/{ticker}")
def get_forward_pe(ticker: str):
    stock = yf.Ticker(ticker.upper())

    pe = None
    try:
        pe = stock.fast_info.get("forwardPE")
    except:
        pass

    return {
        "ticker": ticker.upper(),
        "forwardPE": pe
    }
