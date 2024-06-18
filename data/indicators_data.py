import requests
import pandas as pd
import json
from prettytable import PrettyTable
from data import utils 

## GDP, CPI, PPI, PMI, M0, M1, M2
class get_major_indicators():
    
    def __init__(self):
        
        # outputs
        self.gdp = self.get_gdp()
        self.real_gdp = self.get_real_gdp()
        self.gdp_pct_change = self.get_gdp_pct_change()
        self.ir_10yr = self.get_ir_10yr()
        self.ir_3mo = self.get_ir_3mo()
        self.unemployment_rate = self.get_unemployment_rate()
        self.cpi = self.get_cpi()
        self.ppi = self.get_ppi()
        self.real_m1 = self.get_real_m1()
        self.real_m2 = self.get_real_m2()

        
    def get_gdp(self):

        # Units:  Billions of Dollars, Seasonally Adjusted Annual Rate
        # Frequency:  Quarterly
        # BEA Account Code: A191RC   
        series_id = "GDP"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'value': 'GDP'}, inplace= True)
        
        # GDP breakdown: https://fred.stlouisfed.org/release/tables?rid=53&eid=13026&od=#
        return df
    
    def get_real_gdp(self):

        # Real Gross Domestic Product (Inflation Adjusted)
        # Units:  Billions of Chained 2017 Dollars, Seasonally Adjusted Annual Rate
        # Frequency:  Quarterly
        # BEA Account Code: A191RX

        series_id = "GDPC1"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]

        df.rename(columns = {'value': 'Real_GDP'}, inplace= True)
        
        # Real gross domestic product is the inflation adjusted value of the goods and services produced by labor and property located in the United States.
        # For more information see the Guide to the National Income and Product Accounts of the United States (NIPA). For more information, please visit the Bureau of Economic Analysis.
        
        return df
    
    def get_gdp_pct_change(self):

        # Gross Domestic Product: Implicit Price Deflator
        # Units:  Percent Change from Preceding Period, Seasonally Adjusted Annual Rate
        # Frequency:  Quarterly
        # BEA Account Code: A191RI
        series_id = "A191RI1Q225SBEA"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'value': 'GDP_pct_change'}, inplace= True)
        
        return df

    def get_ir_10yr(self):
    
        # Interest Rates: Long-Term Government Bond Yields: 10-Year: Main (Including Benchmark) for United States
        series_id = "IRLTLT01USM156N"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'date':'Month', 'value': 'Interest_Rate_10yr_Bond'}, inplace= True)
       
        return df
    
    # replace this with t-bill rate
    def get_ir_3mo(self):
    
        # Interest Rates: 3-Month or 90-Day Rates and Yields: Interbank Rates: Total for United States
        series_id = "IR3TIB01USM156N"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'date':'Month', 'value': 'Interest_Rate_3mo_Bond'}, inplace= True)
       
        return df    
    

    def get_unemployment_rate(self):
    
        #search series_id by dataset: https://fredaccount.stlouisfed.org/public/datalist/
        # Unemployment Rate
        series_id = "UNRATE"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'date':'Month', 'value': 'Unemployment_Rate'}, inplace= True)
       
        return df      


    def get_cpi(self):
    
        # Consumer Price Indices (CPIs, HICPs), COICOP 1999: Consumer Price Index: Total for United States
        series_id = "CPALTT01USM659N"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'date':'Month', 'value': 'CPI'}, inplace= True)
       
        return df  
    

    def get_ppi(self):
    
        # Consumer Price Indices (CPIs, HICPs), COICOP 1999: Consumer Price Index: Total for United States
        series_id = "PPIACO"

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'date':'Month', 'value': 'PPI'}, inplace= True)
       
        return df     
    
    # Monetary Metics
    def get_real_m1(self):
    
        # M1 includes funds that are readily accessible for spending. M1 consists of: 
        # (1) currency outside the U.S. Treasury, Federal Reserve Banks, and the vaults of depository institutions; 
        # (2) traveler's checks of nonbank issuers; 
        # (3) demand deposits; and 
        # (4) other checkable deposits (OCDs), which consist primarily of negotiable order of withdrawal (NOW) accounts at depository institutions and credit union share draft accounts. 
        # Seasonally adjusted M1 is calculated by summing currency, traveler's checks, demand deposits, and OCDs, each seasonally adjusted separately.


        # Before May 2020, M1 consists of 
        # (1) currency outside the U.S. Treasury, Federal Reserve Banks, and the vaults of depository institutions; 
        # (2) demand deposits at commercial banks (excluding those amounts held by depository institutions, the U.S. government, and foreign banks and official institutions) less cash items in the process of collection and Federal Reserve float; and 
        # (3) other checkable deposits (OCDs), consisting of negotiable order of withdrawal, or NOW, and automatic transfer service, or ATS, accounts at depository institutions, share draft accounts at credit unions, and demand deposits at thrift institutions.

        # Beginning May 2020, M1 consists of 
        # (1) currency outside the U.S. Treasury, Federal Reserve Banks, and the vaults of depository institutions; 
        # (2) demand deposits at commercial banks (excluding those amounts held by depository institutions, the U.S. government, and foreign banks and official institutions) less cash items in the process of collection and Federal Reserve float; and 
        # (3) other liquid deposits, consisting of OCDs and savings deposits (including money market deposit accounts). 
        # Seasonally adjusted M1 is constructed by summing currency, demand deposits, and OCDs (before May 2020) or other liquid deposits (beginning May 2020), each seasonally adjusted separately.
        
        series_id = "M1REAL" # M1SL M1, seasonally adjusted

        # IRLTLT01USM156N Interest Rates: Long-Term Government Bond Yields: 10-Year: Main (Including Benchmark) for United States

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'date':'Month', 'value': 'Real_M1'}, inplace= True)
       
        return df  
    
    
    def get_real_m2(self):
    
        # M2 includes a broader set of financial assets held principally by households. M2 consists of M1 plus: 
        # (1) savings deposits (which include money market deposit accounts, or MMDAs); 
        # (2) small-denomination time deposits (time deposits in amounts of less than $100,000); and 
        # (3) balances in retail money market mutual funds (MMMFs). 
        # Seasonally adjusted M2 is computed by summing savings deposits, small-denomination time deposits, and retail MMMFs, each seasonally adjusted separately, and adding this result to seasonally adjusted M1.
        
        # Before May 2020, M2 consists of M1 plus 
        # (1) savings deposits (including money market deposit accounts); 
        # (2) small-denomination time deposits (time deposits in amounts of less than $100,000) less individual retirement account (IRA) and Keogh balances at depository institutions; and 
        # (3) balances in retail money market funds (MMFs) less IRA and Keogh balances at MMFs.
        
        # Beginning May 2020, M2 consists of M1 plus 
        # (1) small-denomination time deposits (time deposits in amounts of less than $100,000) less IRA and Keogh balances at depository institutions; and 
        # (2) balances in retail MMFs less IRA and Keogh balances at MMFs. Seasonally adjusted M2 is constructed by summing savings deposits (before May 2020), small-denomination time deposits, and retail MMFs, each seasonally adjusted separately, and adding this result to seasonally adjusted M1.
        
        series_id = "M2REAL"

        # IRLTLT01USM156N Interest Rates: Long-Term Government Bond Yields: 10-Year: Main (Including Benchmark) for United States

        df = utils.fetch_data(series_id)
        df = df[['date','value']]
        df.rename(columns = {'date':'Month', 'value': 'Real_M2'}, inplace= True)
       
        return df  
    
    
    # https://alfred.stlouisfed.org/series?seid=M1V velocity of money
    