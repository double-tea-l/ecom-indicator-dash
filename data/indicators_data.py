import requests
import pandas as pd
import json
from prettytable import PrettyTable
import utils
from prettytable import PrettyTable

class get_major_indicators():
    
    def __init__(self):
        
        # outputs
        self.gdp = self.get_gdp()
        self.real_gdp = self.get_real_gdp()
        self.gdp_pct_change = self.get_gdp_pct_change()

        
    def get_gdp(self):

        # Units:  Billions of Dollars, Seasonally Adjusted Annual Rate
        # Frequency:  Quarterly
        # BEA Account Code: A191RC   
        series_id = "GDP"

        us_gdp = utils.fetch_data(series_id)
        us_gdp = us_gdp[['date','value']]
        us_gdp.rename(columns = {'value': 'GDP'}, inplace= True)
        
        # GDP breakdown: https://fred.stlouisfed.org/release/tables?rid=53&eid=13026&od=#
        return us_gdp
    
    def get_real_gdp(self):

        # Real Gross Domestic Product (Inflation Adjusted)
        # Units:  Billions of Chained 2017 Dollars, Seasonally Adjusted Annual Rate
        # Frequency:  Quarterly
        # BEA Account Code: A191RX

        series_id = "GDPC1"

        us_real_gdp = utils.fetch_data(series_id)
        us_real_gdp = us_real_gdp[['date','value']]

        us_real_gdp.rename(columns = {'value': 'Real_GDP'}, inplace= True)
        
        # Real gross domestic product is the inflation adjusted value of the goods and services produced by labor and property located in the United States.
        # For more information see the Guide to the National Income and Product Accounts of the United States (NIPA). For more information, please visit the Bureau of Economic Analysis.
        
        return us_real_gdp
    
    def get_gdp_pct_change(self):

        #  Gross Domestic Product: Implicit Price Deflator
        # Units:  Percent Change from Preceding Period, Seasonally Adjusted Annual Rate
        # Frequency:  Quarterly
        # BEA Account Code: A191RI
        series_id = "A191RI1Q225SBEA"

        us_gdp_pct_change = utils.fetch_data(series_id)
        us_gdp_pct_change = us_gdp_pct_change[['date','value']]
        us_gdp_pct_change.rename(columns = {'value': 'GDP_pct_change'}, inplace= True)
        
        return us_gdp_pct_change
