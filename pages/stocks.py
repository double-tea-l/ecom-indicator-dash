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
    fig_2 = go.Figure()

    fig_2.add_trace(go.Bar(
        y=df_top_100_stocks['symbol'],
        x=df_top_100_stocks['MarketCap_pct'],
        text=df_top_100_stocks['MarketCap'],
        orientation='h',
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(color='rgba(50, 171, 96, 1.0)', width=1)
        )
    ))

    # Update layout for better visualization
    fig_2.update_layout(
        title='Market Cap Percentage by Company (Top 100)',
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
    
    
    # Display the plots in Streamlit using columns
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_1, use_container_width=True)

    with col2:
        st.plotly_chart(fig_2, use_container_width=True)

# To run the Streamlit app, save this script as `app.py` and run `streamlit run app.py`
