
import yfinance as yf

def get_asia_tech_stocks():
    tickers = ['TSM', 'SSNLF']
    result = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        result[ticker] = hist.to_dict()
    return result
