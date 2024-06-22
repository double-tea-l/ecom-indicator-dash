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
from data import indicators_prep as ind_prep


def show_indicators():
    
    # Get the data
    df_gdp = ind_prep.df_gdp()
    df_cpi_ppi = ind_prep.df_cpi_ppi()

    # Create the first plotly figure for GDP
    fig_gdp = go.Figure()
    fig_gdp.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP'], mode='lines', name='GDP', line=dict(color='red')))
    fig_gdp.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['Real_GDP'], mode='lines', name='Real GDP', line=dict(color='blue')))
    fig_gdp.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP_pct_change'], mode='lines', name='GDP % Change', line=dict(color='green', dash='dot'), yaxis='y2'))

    fig_gdp.update_layout(
        title='GDP and Real GDP Over Time',
        xaxis_title='Time Period',
        yaxis_title='$ Billions',
        yaxis=dict(tickformat=','),
        xaxis=dict(type='date'),
        yaxis2=dict(
            title='GDP % Change',
            overlaying='y',
            side='right',
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
    fig_gdp.update_xaxes(tickangle=0)

    # Create the second plotly figure for CPI and PPI
    fig_cpi_ppi = go.Figure()
    fig_cpi_ppi.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['CPI'], mode='lines', name='CPI', line=dict(color='red')))
    fig_cpi_ppi.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['PPI'], mode='lines', name='PPI', line=dict(color='blue')))
  
    fig_cpi_ppi.update_layout(
        title='CPI and PPI Over Time',
        xaxis_title='Time Period',
        yaxis_title='Index Value',
        yaxis=dict(tickformat=','),
        xaxis=dict(type='date'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    fig_cpi_ppi.update_xaxes(tickangle=0)

    # Display the plots in Streamlit using columns
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_gdp, use_container_width=True)

    with col2:
        st.plotly_chart(fig_cpi_ppi, use_container_width=True)