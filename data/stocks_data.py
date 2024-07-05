import pandas as pd
import yfinance as yf
import requests
import re
import json

class get_stock_data():
    
    def __init__(self):
        
        self.all_stocks = self.get_all_stocks()
        self.top_industries = self.get_top_industries()
        self.top_100_stocks = self.get_top_100_stocks()
        self.top_stocks_by_group = self.get_top_stocks_by_group()
    # self.real_gdp = self.get_real_gdp()

    def get_all_stocks(self):
    
        urls = {
            "Nasdaq": 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nasdaq/nasdaq_full_tickers.json',
            "NYSE": 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nyse/nyse_full_tickers.json',
            "AMEX": 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/amex/amex_full_tickers.json'
        }

        # Now urls is a dictionary with the keys "Nasdaq", "NYSE", and "AMEX" each associated with their respective URL
        print(urls)

        # Fetch the content of the JSON file
        df_all_stocks = pd.DataFrame()

        for key, url in urls.items():
            response = requests.get(url)
            df_tmp = pd.DataFrame(response.json())
            df_tmp['Exchange'] = key
            df_all_stocks = pd.concat([df_all_stocks, df_tmp], ignore_index = True)

        df_all_stocks['marketCap'] = pd.to_numeric(df['marketCap'], errors='coerce')
        df_all_stocks['marketCap'] = df_all_stocks['marketCap'].fillna(0)
        df_all_stocks['marketCap'] = df_all_stocks['marketCap'].astype(int)

        df_all_stocks = df_all_stocks.sort_values(by=['marketCap'], ascending= False).reset_index(drop = True)
        df_all_stocks['MarketCap_pct'] = df['marketCap'] / df_all_stocks['marketCap'].sum()
        df_all_stocks['MarketCap_pct_cumsum'] = df_all_stocks['MarketCap_pct'].cumsum()

        # Fill empty values in 'industry' and 'sector' columns with 'Other'
        df_all_stocks['industry'].replace('', 'Other', inplace=True)
        df_all_stocks['sector'].replace('', 'Other', inplace=True)

        return df_all_stocks 
    
    def get_top_industries(self):
        
        df_all_stocks = self.df_all_stocks
        
        sorted_industry_marketcap_sum = df_all_stocks.groupby('industry').agg({
            'MarketCap_pct': 'sum',
            'marketCap': 'sum'
        }).reset_index().sort_values(by='MarketCap_pct', ascending=False)

        # sorted_industry_marketcap_sum = sorted_industry_marketcap_sum[sorted_industry_marketcap_sum['MarketCap_pct']>.01]

        sorted_industry_marketcap_sum['MarketCap_pct_cumsum'] = sorted_industry_marketcap_sum['MarketCap_pct'].cumsum()

        # Filter industries where MarketCap_pct_cumsum is >= 85%
        top_industries = sorted_industry_marketcap_sum[
            (sorted_industry_marketcap_sum['MarketCap_pct_cumsum'] <= .9) &  # Cumulative sum condition
            (sorted_industry_marketcap_sum['industry'] != "")  # Ensure industry is not empty
        ]

        top_industries.reset_index(drop = True, inplace = True)
    
        return top_industries
    

    def get_top_100_stocks(self):
        
        df = self.df_all_stocks
        
        top_100_stocks = df.head(100)
    
        return top_100_stocks


    def get_top_stocks_by_group(self):
        
        df = self.df_all_stocks
        
        top_10_stocks_per_industry = df.groupby('industry').apply(lambda x: x.nlargest(10, 'marketCap')).reset_index(drop=True)
        top_10_stocks_per_sector = df.groupby('sector').apply(lambda x: x.nlargest(10, 'marketCap')).reset_index(drop=True)
        
        top_10_stocks_per_industry['Categorty'] = 'Top_10_Stocks_per_Industry'
        top_10_stocks_per_industry['Categorty'] = 'Top_10_Stocks_per_Sector'
        
        top_stocks_by_group = pd.concat(top_10_stocks_per_industry, top_10_stocks_per_sector)
    
        return top_stocks_by_group
