# main.py

import streamlit as st
from app.components.sidebar import sidebar
from app.components.main_view import main_view

def main():
    st.title("Predictive Maintenance Dashboard")
    data_file = sidebar()
    main_view(data_file)

if __name__ == "__main__":
    main()
