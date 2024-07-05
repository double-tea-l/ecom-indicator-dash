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
import plotly_express as px


def show_stocks():

    df = sp.df_top_industries_by_market_cap()

    # Create the bar plot
    fig = px.bar(df.head(15), y='industry', x='MarketCap_pct', 
                title='Market Cap Percentage by Industry (Top 10)',
                labels={'industry': '', 'MarketCap_pct': 'Market Cap Percentage'},
                orientation='h',
                height=450,
                text='MarketCap')  # Adding the formatted MarketCap as text labels

    # Update layout to ensure x-axis labels fit and bars are sorted
    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},  # Ensures bars are sorted by MarketCap_pct in descending order
        xaxis_tickangle=0,  # Adjusts x-axis label angle to fit long strings
        margin=dict(l=250, r=50)  # Adds left margin to accommodate long industry names
    )

    # Show the plot
    fig.show()
