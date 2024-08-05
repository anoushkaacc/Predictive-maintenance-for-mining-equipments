import streamlit as st
def sidebar():
  st.sidebar.title("Predictive Maintenance Dashboard")
  st.sidebar.subheader("Settings")
  data_file=st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
  return data_file