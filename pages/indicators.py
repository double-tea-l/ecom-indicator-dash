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


    # st.title('Economics Indicator Dashboard')

    df_gdp = ind_prep.df_gdp()

    # Create the plotly figure
    fig = go.Figure()

    # Add trace for GDP
    fig.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP'], mode='lines', name='GDP', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['Real_GDP'], mode='lines', name='Real GDP', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP_pct_change'], mode='lines', name='GDP % Change', line=dict(color='green', dash='dot'), yaxis='y2'))

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
    
    #  # st.title('Economics Indicator Dashboard')

    # df_cpi_ppi = ind_prep.df_cpi_ppi()

    # # Create the plotly figure
    # fig2 = go.Figure()

    # # Add trace for GDP
    # fig2.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['CPI'], mode='lines', name='CPI', line=dict(color='red')))
    # fig2.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['PPI'], mode='lines', name='PPI', line=dict(color='blue')))
  
    # # Update layout for secondary y-axis
    # fig2.update_layout(
    #     title='GDP and Real GDP Over Time',
    #     xaxis_title='Time Period',
    #     yaxis_title='$ Billions',
    #     yaxis=dict(tickformat=','),
    #     xaxis=dict(type='date'),
    #     yaxis2=dict(
    #         title='GDP % Change',
    #         overlaying='y',
    #         side='right',
    #         showgrid=False,
    #         zeroline=False
    #     ),
    #     legend=dict(
    #         orientation="h",
    #         yanchor="bottom",
    #         y=1.02,
    #         xanchor="right",
    #         x=1
    #     )
    # )

    # # Rotate x-axis labels for better readability
    # fig2.update_xaxes(tickangle=0)

    # # Display the plot in Streamlit
    # st.plotly_chart(fig2, use_container_width=True)   
    
    
    
    


# # # Call the function to show indicators
# # show_indicators()


# import streamlit as st
# import plotly.graph_objects as go
# from data import indicators_prep as ind_prep

# def show_indicators():
#     st.title('Economic Indicators Dashboard')

#     # GDP and Real GDP Chart
#     df_gdp = ind_prep.df_gdp()
    
#     fig1 = go.Figure()

#     fig1.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP'], mode='lines', name='GDP', line=dict(color='red')))
#     fig1.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['Real_GDP'], mode='lines', name='Real GDP', line=dict(color='blue')))
#     fig1.add_trace(go.Scatter(x=df_gdp['date'], y=df_gdp['GDP_pct_change'], mode='lines', name='GDP % Change', line=dict(color='green', dash='dot'), yaxis='y2'))

#     fig1.update_layout(
#         title='GDP and Real GDP Over Time',
#         xaxis_title='Time Period',
#         yaxis_title='$ Billions',
#         yaxis=dict(tickformat=','),
#         xaxis=dict(type='date'),
#         yaxis2=dict(
#             title='GDP % Change',
#             overlaying='y',
#             side='right',
#             showgrid=False,
#             zeroline=False
#         ),
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         )
#     )

#     fig1.update_xaxes(tickangle=0)

#     st.plotly_chart(fig1, use_container_width=True)
    
#     # CPI and PPI Chart
#     df_cpi_ppi = ind_prep.df_cpi_ppi()

#     fig2 = go.Figure()

#     fig2.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['CPI'], mode='lines', name='CPI', line=dict(color='red')))
#     fig2.add_trace(go.Scatter(x=df_cpi_ppi['date'], y=df_cpi_ppi['PPI'], mode='lines', name='PPI', line=dict(color='blue')))
  
#     fig2.update_layout(
#         title='CPI and PPI Over Time',
#         xaxis_title='Time Period',
#         yaxis_title='Index Value',
#         yaxis=dict(tickformat=','),
#         xaxis=dict(type='date'),
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         )
#     )

#     fig2.update_xaxes(tickangle=0)

#     st.plotly_chart(fig2, use_container_width=True)

# # Call the function to show indicators
# if __name__ == "__main__":
#     show_indicators()
