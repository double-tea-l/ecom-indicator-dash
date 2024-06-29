import pandas as pd
import yfinance as yf
import requests
import re
import json

class get_stock_data():
    
    def __init__(self):
        
        self.market_cap = self.get_market_cap()
    # self.real_gdp = self.get_real_gdp()

    def get_market_cap(self):
    
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



        df['marketCap'] = pd.to_numeric(df['marketCap'], errors='coerce')
        df['marketCap'] = df['marketCap'].fillna(0)
        df['marketCap'] = df['marketCap'].astype(int)

        df = df.sort_values(by=['marketCap'], ascending= False).reset_index(drop = True)
        df['MarketCap_pct'] = df['marketCap'] / df['marketCap'].sum()
        df['MarketCap_pct_cumsum'] = df['MarketCap_pct'].cumsum()

        sorted_industry_marketcap_sum = df.groupby('industry').agg({
            'MarketCap_pct': 'sum',
            'marketCap': 'sum'
        }).reset_index().sort_values(by='MarketCap_pct', ascending=False)

        # sorted_industry_marketcap_sum = sorted_industry_marketcap_sum[sorted_industry_marketcap_sum['MarketCap_pct']>.01]

        sorted_industry_marketcap_sum['MarketCap_pct_cumsum'] = sorted_industry_marketcap_sum['MarketCap_pct'].cumsum()

        # Filter industries where MarketCap_pct_cumsum is >= 85%
        filtered_df = sorted_industry_marketcap_sum[
            (sorted_industry_marketcap_sum['MarketCap_pct_cumsum'] <= .9) &  # Cumulative sum condition
            (sorted_industry_marketcap_sum['industry'] != "")  # Ensure industry is not empty
        ]

        filtered_df.reset_index(drop = True, inplace = True)

        filtered_df
        
        return filtered_df