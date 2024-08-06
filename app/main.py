# app/main.py

import streamlit as st
from .components.sidebar import sidebar
from .components.main_view import main_view
import logging

logging.basicConfig(level=logging.DEBUG)
def main():
    st.title("Predictive Maintenance Dashboard")
    data_file = sidebar()
    logging.debug(f"Data file uploaded: {data_file}")
    main_view(data_file)

if __name__ == "__main__":
    main()