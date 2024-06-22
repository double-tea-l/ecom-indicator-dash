
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
    cpi = i.cpi
    ppi = i.ppi
    
        # format
    df_cpi_ppi = pd.merge(cpi, ppi, on = 'date', how = 'outer')
    df_cpi_ppi = df_cpi_ppi.sort_values(by='date', ascending= True).reset_index(drop = True)
    df_cpi_ppi['Month'] = pd.to_datetime(df_cpi_ppi['date'])

    # # Convert 'GDP' and 'Real_GDP' columns to numeric, coercing errors
    # df_cpi_ppi['CPI'] = pd.to_numeric(df_cpi_ppi['CPI'], errors='coerce')
    # df_cpi_ppi['PPI'] = pd.to_numeric(df_cpi_ppi['PPI'], errors='coerce')
    # # Round up GDP values to integers
    # df_cpi_ppi['CPI'] = df_cpi_ppi['CPI'].apply(lambda x: math.ceil(x) if pd.notnull(x) else x)
    # df_cpi_ppi['PPI'] = df_cpi_ppi['PPI'].apply(lambda x: math.ceil(x) if pd.notnull(x) else x)
    
    return df_cpi_ppi


def df_interest_rate():

    i = indicators.get_major_indicators()
    ir_10yr = i.ir_10yr
    ir_3mo = i.ir_3mo
    
    df_ir = pd.merge(ir_10yr, ir_3mo, on = 'date', how = 'outer')
    df_ir = df_ir.sort_values(by='date', ascending= True).reset_index(drop = True)
    df_ir['Month'] = pd.to_datetime(df_ir['date']) 
    
    return df_ir


def df_unemployment_rate():

    i = indicators.get_major_indicators()
    unemployment_rate = i.unemployment_rate

    df_ur = unemployment_rate.sort_values(by='date', ascending= True).reset_index(drop = True)
    df_ur['Month'] = pd.to_datetime(df_ur['date']) 
    
    return df_ur



def df_real_m1_m2():

    i = indicators.get_major_indicators()
    real_m1 = i.real_m1
    real_m2 = i.real_m2

    df_real_m1_m2 = pd.merge(real_m1, real_m2, on = 'date', how = 'outer')
    df_real_m1_m2 = df_real_m1_m2.sort_values(by='date', ascending= True).reset_index(drop = True)
    df_real_m1_m2['Month'] = pd.to_datetime(df_real_m1_m2['date']) 
    
    return df_real_m1_m2


