
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
import os


# st.set_page_config(initial_sidebar_state="collapsed")
# Set the page config at the start of the main script
st.set_page_config(
    page_title="Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="collapsed"
)


pages = ["Indicators", "Stock Index", "Knowledge", "Resources", "GitHub"]

parent_dir = os.path.dirname(os.path.abspath(__file__))

# logo_path = os.path.join(parent_dir, "cubes.svg")

urls = {"GitHub": "https://github.com/double-tea-l/ecom-indicator-dash/"}

styles = {
    "nav": {
        "background-color": "grey",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        # "color": "var(--text-color)",
        "color": "grey",
        "font-weight": "normal",
        "padding": "14px",
    }
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    # logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Indicators": pg.show_indicators,
    "Stock Index": pg.show_stocks
}
go_to = functions.get(page)
if go_to:
    go_to()