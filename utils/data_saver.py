# data_saver.py

import pandas as pd
import joblib
import os

def save_data(data, file_path):
    """
    Save data to a CSV file.

    Parameters:
    - data (DataFrame): The data to save.
    - file_path (str): The path to save the CSV file.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

def save_model(model, file_path):
    """
    Save a trained model to a file.

    Parameters:
    - model: The trained model to save.
    - file_path (str): The path to save the model.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")
