import pandas as pd
import yfinance as yf
import requests
import re
import json


urls = {
    "Nasdaq": 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nasdaq/nasdaq_full_tickers.json',
    "NYSE": 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nyse/nyse_full_tickers.json',
    "AMEX": 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/amex/amex_full_tickers.json'
}

# Now urls is a dictionary with the keys "Nasdaq", "NYSE", and "AMEX" each associated with their respective URL
print(urls)

# Fetch the content of the JSON file
df = pd.DataFrame()

for key, url in urls.items():
    response = requests.get(url)
    df_tmp = pd.DataFrame(response.json())
    df_tmp['Exchange'] = key
    df = pd.concat([df, df_tmp], ignore_index = True)

# save a local copy
# df.to_csv('us_symbol_tickers.csv', index = False)
df.head()