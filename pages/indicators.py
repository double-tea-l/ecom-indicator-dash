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
from ..pages import ecom_indicators_data as ind


st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

page = st_navbar(["Major Indicators", "Stock Index", "Knowledge", "About"])
st.write(page)


st.title('Economics Indicator Dashboard')


data = ind.df_gdp

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