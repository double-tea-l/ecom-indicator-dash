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


def show_stocks():
    
    # CPI and PPI Chart
    df_cpi_ppi = ind_prep.df_cpi_ppi()

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['CPI'], mode='lines', name='CPI', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['PPI'], mode='lines', name='PPI', line=dict(color='blue')))
  
    fig.update_layout(
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

    fig.update_xaxes(tickangle=0)

    st.plotly_chart(fig, use_container_width=True)

# # Call the function to show indicators
# if __name__ == "__main__":
#     show_stocks()
