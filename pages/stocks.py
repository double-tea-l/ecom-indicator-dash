import requests
import pandas as pd
import numpy as np
import math
import prettytable
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.graph_objects as go
from streamlit_navigation_bar import st_navbar
from data import stocks_prep as sp

def show_stocks():
    
    df_top_industries = sp.df_top_industries_by_market_cap()

    # Sort data by MarketCap_pct to ensure correct order
    df_top_industries = df_top_industries.sort_values('MarketCap_pct', ascending=True)

    # Create a bar plot using Plotly Graph Objects
    fig_1 = go.Figure()

    fig_1.add_trace(go.Bar(
        y=df_top_industries['industry'],
        x=df_top_industries['MarketCap_pct'],
        text=df_top_industries['MarketCap'],
        orientation='h',
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(color='rgba(50, 171, 96, 1.0)', width=1)
        )
    ))

    # Update layout for better visualization
    fig_1.update_layout(
        title='Market Cap Percentage by Industry (Top 15)',
        xaxis=dict(
            title='Market Cap Percentage',
            tickangle=0
        ),
        yaxis=dict(
            title='',
            categoryorder='total ascending'  # Ensure bars are sorted by MarketCap_pct
        ),
        margin=dict(l=250, r=50),  # Add left margin to accommodate long industry names
        height=450
    )


    df_top_100_stocks = sp.df_top_100_stocks()
     # Create a bar plot using Plotly Graph Objects

    # Create a table using Plotly Graph Objects
    fig_2 = go.Figure(data=[go.Table(
        header=dict(
            values=list(df_top_100_stocks.columns),
            fill_color='paleturquoise',
            align='left'
        ),
        cells=dict(
            values=[df_top_100_stocks[col].tolist() for col in df_top_100_stocks.columns],
            fill_color='lavender',
            align='left'
        )
    )])

    # Update layout for better visualization and scrolling
    fig_2.update_layout(
        title='Top 100 Stocks Information',
        height=600,  # Adjust height as needed
        margin=dict(l=0, r=0, b=0, t=50),  # Adjust margins as needed
    )

    df_top_stocks_by_group = sp.df_top_stocks_by_group()
    # Streamlit app
    # st.title('Stock Symbols by Industry and Sector')

    # Filters
    selected_industry = st.selectbox('Select Industry', options=['All'] + sorted(df_top_stocks_by_group['industry'].unique().tolist()))
    selected_sector = st.selectbox('Select Sector', options=['All'] + sorted(df_top_stocks_by_group['sector'].unique().tolist()))

    # Filtering logic
    if selected_industry != 'All':
        df_top_stocks_by_group = df_top_stocks_by_group[df_top_stocks_by_group['industry'] == selected_industry]

    if selected_sector != 'All':
        df_top_stocks_by_group = df_top_stocks_by_group[df_top_stocks_by_group['sector'] == selected_sector]

    # Plotly table
    fig_3 = go.Figure(data=[go.Table(
        header=dict(values=list(df_top_stocks_by_group.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df_top_stocks_by_group.symbol, df_top_stocks_by_group.industry, df_top_stocks_by_group.sector],
                fill_color='lavender',
                align='left'))
    ])


    # Display the table
    st.plotly_chart(fig_1, use_container_width=True)
    st.plotly_chart(fig_2, use_container_width=True)
    st.plotly_chart(fig_3, use_container_width=True)

# To run the Streamlit app, save this script as `app.py` and run `streamlit run app.py`
