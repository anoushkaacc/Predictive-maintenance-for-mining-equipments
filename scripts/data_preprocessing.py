# data_preprocessing.py

import pandas as pd
import os

def preprocess_data():
    # Load raw data
    raw_data_path = r'C:\Users\anoushka chatterjee\Desktop\project\data\raw\equipment_data.csv'
    raw_data = pd.read_csv(raw_data_path)
    
    # Basic preprocessing steps
    # Example: Fill missing values (if any), remove unnecessary columns, etc.
    raw_data.fillna(method='ffill', inplace=True)  # Fill missing values as an example
    
    # Ensure the target column exists
    if 'failure' not in raw_data.columns:
        raise KeyError("The target column 'failure' is missing from the raw data")
    
    # Save preprocessed data
    os.makedirs('data/processed', exist_ok=True)
    preprocessed_data_path = 'data/processed/preprocessed_data.csv'
    raw_data.to_csv(preprocessed_data_path, index=False)
    print(f'Preprocessed data saved to {preprocessed_data_path}')

if __name__ == '__main__':
    preprocess_data()
