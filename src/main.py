from fastapi import FastAPI
import requests

app = FastAPI(title="Kasparro Backend ETL")

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"
COINPAPRIKA_URL = "https://api.coinpaprika.com/v1/tickers"


@app.get("/")
def root():
    return {"message": "Kasparro Backend is running"}


@app.get("/prices")
def get_crypto_prices():
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1
    }

    coingecko_data = requests.get(COINGECKO_URL, params=params).json()
    coinpaprika_data = requests.get(COINPAPRIKA_URL).json()[:5]

    return {
        "coingecko": coingecko_data,
        "coinpaprika": coinpaprika_data
    }
