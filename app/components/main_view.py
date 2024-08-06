import streamlit as st
from data_loader import load_data
from data_visualization import plot_feature_correlations

def main():
    load_data()
    plot_feature_correlations()


def main_view(data_file):
    if data_file:
        data = load_data(data_file)
        st.write("Data Overview")
        st.write(data.head())
        
        st.write("Feature Correlations")
        plot_feature_correlations(data)
