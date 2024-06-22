
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
import os


from pages import indicators, stocks

pages = {
    'Indicators': indicators
    , 'Stocks': stocks
}

st.sidebar.title('Navigation')

choice = st.sidebar.radio("Choose a page:", list(pages.keys()))

page = pages[choice]

page.app()