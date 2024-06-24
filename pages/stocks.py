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

    df = pd.DataFrame({
        "Index": ['SP500', 'DJIA', 'NASDAQ100'],
        "Composition": ["500 Companies", "30 Blue-chip Companies", "100 Companies"],
        "Market_Value": ['70-80% US Market','25%',' '],
        "Method": ['Market Value Weighted Avg','Price Weighted Average','']
    })

    true_html = '<input type="checkbox" checked disabled="true">'
    false_html = '<input type="checkbox" disabled="true">'

    # df['D'] = df['D'].apply(lambda b: true_html if b else false_html)

    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

    # txt = st.text_area(
    # "Text to analyze",
    # "It was the best of times, it was the worst of times, it was the age of "
    # "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    # "was the epoch of incredulity, it was the season of Light, it was the "
    # "season of Darkness, it was the spring of hope, it was the winter of "
    # "despair, (...)",
    # )

    # st.write(f"You wrote {len(txt)} characters.")

# # Call the function to show indicators
# if __name__ == "__main__":
#     show_stocks()
