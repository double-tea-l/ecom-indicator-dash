import pandas as pd
import math
from prettytable import PrettyTable
from data import stocks_data as sd



def df_top_industries_by_market_cap():
    
    i = sd.get_stock_data()
    
        # Function to format MarketCap values
    def format_marketcap(value):
        if value >= 1_000_000_000_000:
            return f"${value/1_000_000_000_000:.1f}T"
        elif value >= 1_000_000_000:
            return f"${value/1_000_000_000:.1f}B"
        elif value >= 1_000_000:
            return f"${value/1_000_000:.1f}M"
        else:
            return f"${value:.1f}K"


    top_industries = i.get_top_industries()
    
    top_industries['MarketCap'] = top_industries['marketCap'].apply(format_marketcap)
    
    return top_industries

     # all_stocks = i.get_all_stocks()   
    # top_industries = i.get_top_industries()
    # top_100_stocks = i.get_top_100_stocks()
    # top_stocks_by_group = i.get_top_stocks_by_group()