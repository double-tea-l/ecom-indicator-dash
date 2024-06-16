import requests
import pandas as pd
import json
import prettytable
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.graph_objects as go
import numpy as np
import math
from streamlit_navigation_bar import st_navbar



def fetch_series_data(series_id, api_key):
    """Fetch observations for a FRED series and save to a DataFrame."""
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json"
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        observations = data.get('observations', [])
        # Create DataFrame
        df = pd.DataFrame(observations)
        # Display the DataFrame
        return df
        # Save DataFrame to CSV
        # df.to_csv(f'{series_id}_observations.csv', index=False)
        # print(f"Data saved to {series_id}_observations.csv")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}, Error: {response.text}")

# Replace 'your_real_api_key' with your actual FRED API key
api_key = "9648695895d3facac4fba9c7cb834427"

#  Gross Domestic Product: Implicit Price Deflator
series_id = "A191RI1Q225SBEA"
# Units:  Percent Change from Preceding Period, Seasonally Adjusted Annual Rate
# Frequency:  Quarterly
# BEA Account Code: A191RI
us_gdp_pct_change = fetch_series_data(series_id, api_key)
us_gdp_pct_change = us_gdp_pct_change[['date','value']]
us_gdp_pct_change.rename(columns = {'value': 'GDP_pct_change'}, inplace= True)

#  Real Gross Domestic Product (Inflation Adjusted)
series_id = "GDPC1"
# Units:  Billions of Chained 2017 Dollars, Seasonally Adjusted Annual Rate
# Frequency:  Quarterly
# BEA Account Code: A191RX
# Real gross domestic product is the inflation adjusted value of the goods and services produced by labor and property located in the United States.
# For more information see the Guide to the National Income and Product Accounts of the United States (NIPA). For more information, please visit the Bureau of Economic Analysis.
us_real_gdp = fetch_series_data(series_id, api_key)
us_real_gdp = us_real_gdp[['date','value']]
# us_real_gdp['value'] = us_real_gdp['value'].apply(lambda x: math.ceil(x))
us_real_gdp.rename(columns = {'value': 'Real_GDP'}, inplace= True)

# Interest Rates: Long-Term Government Bond Yields: 10-Year: Main (Including Benchmark) for United States
series_id = "GDP"
# breakdown: https://fred.stlouisfed.org/release/tables?rid=53&eid=13026&od=#
# Units:  Billions of Dollars, Seasonally Adjusted Annual Rate
# Frequency:  Quarterly
# BEA Account Code: A191RC
us_gdp = fetch_series_data(series_id, api_key)
us_gdp = us_gdp[['date','value']]
# us_gdp['value'] = us_gdp['value'].apply(lambda x: math.ceil(x))
us_gdp.rename(columns = {'value': 'GDP'}, inplace= True)


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


# print(df_gdp)




st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

page = st_navbar(["Major Indicators", "Stock Index", "Knowledge", "About"])
st.write(page)


st.title('Economics Indicator Dashboard')


data = df_gdp

# Create the plotly figure
fig = go.Figure()

# Add trace for GDP
fig.add_trace(go.Scatter(x=data['date'], y=data['GDP'], mode='lines', name='GDP', line=dict(color='red')))

# Add trace for Real GDP
fig.add_trace(go.Scatter(x=data['date'], y=data['Real_GDP'], mode='lines', name='Real GDP', line=dict(color='blue')))

# Add trace for GDP percentage change on secondary y-axis
fig.add_trace(go.Scatter(x=data['date'], y=data['GDP_pct_change'], mode='lines', name='GDP % Change', line=dict(color='green', dash='dot'), yaxis='y2'))

# Update layout for secondary y-axis
fig.update_layout(
    title='GDP and Real GDP Over Time',
    xaxis_title='Time Period',
    yaxis_title='$ Billions',
    yaxis=dict(tickformat=','),
    xaxis=dict(type='date'),
    yaxis2=dict(
        title='GDP % Change',
        overlaying='y',
        side='right',
        # tickformat=',.2%'
        showgrid=False,
        zeroline=False
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
    
)

# Rotate x-axis labels for better readability
fig.update_xaxes(tickangle=0)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)