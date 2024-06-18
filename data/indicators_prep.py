
import pandas as pd
import math
from prettytable import PrettyTable
from data import indicators_data as indicators



def df_gdp():
    
    i = indicators.get_major_indicators()
    
    #inputs
    us_gdp_pct_change = i.gdp_pct_change
    us_gdp = i.gdp
    us_real_gdp = i.real_gdp
     
    # format
    df_gdp = pd.merge(us_gdp_pct_change, us_gdp, on = 'date', how = 'outer')
    df_gdp = pd.merge(df_gdp, us_real_gdp, on = 'date', how = 'outer')
    df_gdp = df_gdp.sort_values(by='date', ascending= True).reset_index(drop = True)
    df_gdp['date'] = pd.to_datetime(df_gdp['date'])
    # Function to convert date to quarter
    def date_to_quarter(date):
        return f"{date.year} Q{((date.month - 1) // 3) + 1}"
    # Apply the function to the dataframe
    df_gdp['Quarter'] = df_gdp['date'].apply(date_to_quarter)
    df_gdp = df_gdp[df_gdp['date']>='1948-01-01']
    # Convert 'GDP' and 'Real_GDP' columns to numeric, coercing errors
    df_gdp['GDP'] = pd.to_numeric(df_gdp['GDP'], errors='coerce')
    df_gdp['Real_GDP'] = pd.to_numeric(df_gdp['Real_GDP'], errors='coerce')

    # Round up GDP values to integers
    df_gdp['GDP'] = df_gdp['GDP'].apply(lambda x: math.ceil(x) if pd.notnull(x) else x)
    df_gdp['Real_GDP'] = df_gdp['Real_GDP'].apply(lambda x: math.ceil(x) if pd.notnull(x) else x)
    
    return df_gdp


def df_cpi_ppi():
    
    i = indicators.get_major_indicators()
    cpi = i.get_cpi
    ppi = i.get_ppi
    
        # format
    df_cpi_ppi = pd.merge(cpi, ppi, on = 'date', how = 'outer')
    df_cpi_ppi = df_cpi_ppi.sort_values(by='date', ascending= True).reset_index(drop = True)
    df_cpi_ppi['Month'] = pd.to_datetime(df_cpi_ppi['date'])

    # Convert 'GDP' and 'Real_GDP' columns to numeric, coercing errors
    df_cpi_ppi['CPI'] = pd.to_numeric(df_cpi_ppi['CPI'], errors='coerce')
    df_cpi_ppi['PPI'] = pd.to_numeric(df_cpi_ppi['PPI'], errors='coerce')
    # Round up GDP values to integers
    df_cpi_ppi['CPI'] = df_cpi_ppi['CPI'].apply(lambda x: math.ceil(x) if pd.notnull(x) else x)
    df_cpi_ppi['PPI'] = df_cpi_ppi['PPI'].apply(lambda x: math.ceil(x) if pd.notnull(x) else x)
    
    return df_cpi_ppi