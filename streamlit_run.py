
import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed")


from streamlit_navigation_bar import st_navbar
import pages as pg
import os

# Set the page config at the start of the main script
# st.set_page_config(
#     page_title="US Population Dashboard",
#     page_icon="🏂",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )


pages = ["Indicators", "User Guide", "API", "Examples", "Community", "GitHub"]

parent_dir = os.path.dirname(os.path.abspath(__file__))

# logo_path = os.path.join(parent_dir, "cubes.svg")

urls = {"GitHub": "https://github.com/double-tea-l/ecom-indicator-dash/"}

styles = {
    "nav": {
        "background-color": "royalblue",
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
        "color": "var(--text-color)",
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
    "Indicators": pg.show_indicators
}
go_to = functions.get(page)
if go_to:
    go_to()