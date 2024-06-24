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
from st_aggrid import AgGrid, GridOptionsBuilder


def show_indicators():
    
    # Get the data
    df_gdp = ind_prep.df_gdp()
    df_cpi_ppi = ind_prep.df_cpi_ppi()
    df_interest_rate = ind_prep.df_interest_rate()
    df_unemployment_rate = ind_prep.df_unemployment_rate()
    df_real_m1_m2 = ind_prep.df_real_m1_m2()

    # Create figure for GDP
    fig_gdp = go.Figure()
    fig_gdp.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP'], mode='lines', name='GDP', line=dict(color='#008080')))
    fig_gdp.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['Real_GDP'], mode='lines', name='Real GDP', line=dict(color='#4682B4')))
    fig_gdp.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP_pct_change'], mode='lines', name='GDP % Change', line=dict(color='#483D8B', dash='dot'), yaxis='y2'))

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
    
    # GDP table
    fig_gdp_table = go.Figure(data=[go.Table(
    header=dict(values=list(df_gdp[['Quarter','GDP','Real_GDP','GDP_pct_change']].columns),
                fill_color='white',
                align='left'),
    cells=dict(values=[df_gdp.Quarter, df_gdp.GDP, df_gdp.Real_GDP, df_gdp.GDP_pct_change],
            #    fill_color='lavender',
               align='left'))
                ])


    # Create figure for CPI and PPI
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


     # Create figure for Interest Rates
    fig_interest_rate = go.Figure()
    fig_interest_rate.add_trace(go.Scatter(x=df_interest_rate['date'], y=df_interest_rate['Interest_Rate_10yr'], mode='lines', name='Interest Rate: 10 years', line=dict(color='red')))
    fig_interest_rate.add_trace(go.Scatter(x=df_interest_rate['date'], y=df_interest_rate['Interest_Rate_3mo'], mode='lines', name='Interest Rate: 3 months', line=dict(color='blue')))
  
    fig_interest_rate.update_layout(
        title='Interest Rate',
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
    fig_interest_rate.update_xaxes(tickangle=0)   
    
    
    
     # Create figure for Unemployment Rate
    fig_unrate = go.Figure()
    fig_unrate.add_trace(go.Scatter(x=df_unemployment_rate['date'], y=df_unemployment_rate['Unemployment_Rate'], mode='lines', name='Unemployment Rate', line=dict(color='red')))

    fig_unrate.update_layout(
        title='Unemployment Rate',
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
    fig_unrate.update_xaxes(tickangle=0)   
    
    
     # Create figure for Interest Rates
    fig_real_m1_m2 = go.Figure()
    fig_real_m1_m2.add_trace(go.Scatter(x=df_real_m1_m2['date'], y=df_real_m1_m2['Real_M1'], mode='lines', name='Real M1', line=dict(color='red')))
    fig_real_m1_m2.add_trace(go.Scatter(x=df_real_m1_m2['date'], y=df_real_m1_m2['Real_M2'], mode='lines', name='Real M2', line=dict(color='blue')))
  
    fig_real_m1_m2.update_layout(
        title='Real M1 and M2',
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
    fig_real_m1_m2.update_xaxes(tickangle=0)  
    # df_real_m1_m2 = ind_prep.df_real_m1_m2()



    # Display the plots in Streamlit using columns
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_gdp, use_container_width=True)

    with col2:
        
         st.plotly_chart(fig_gdp_table, use_container_width=True)
        # st.plotly_chart(fig_cpi_ppi, use_container_width=True)
        
        # Second row with two columns
    col3, col4 = st.columns(2)
    
    with col3:
        st.plotly_chart(fig_interest_rate, use_container_width=True)

    with col4:
        st.plotly_chart(fig_real_m1_m2, use_container_width=True)