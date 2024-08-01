# feature_engineering.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

def engineer_features():
    # Load preprocessed data
    preprocessed_data_path = 'data/processed/preprocessed_data.csv'
    data = pd.read_csv(preprocessed_data_path)
    
    # Debug: Print columns to verify target column existence
    print("Columns in preprocessed data:", data.columns)
    
    # Ensure the target column exists
    if 'target' not in data.columns:
        raise KeyError("The target column is missing from the preprocessed data")
    
    # Feature engineering steps
    # Example: Create new features, encode categorical variables, scale features, etc.
    # Assuming 'target' is the column to predict and should be excluded from scaling
    target = data['target']
    features = data.drop('target', axis=1)
    
    # Scaling features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # Create DataFrame with scaled features
    scaled_data = pd.DataFrame(scaled_features, columns=features.columns)
    scaled_data['target'] = target
    
    # Split into train and test sets (80% train, 20% test)
    train_data = scaled_data.sample(frac=0.8, random_state=42)
    test_data = scaled_data.drop(train_data.index)
    
    # Save processed data
    os.makedirs('data/processed', exist_ok=True)
    train_data.to_csv('data/processed/train_data.csv', index=False)
    test_data.to_csv('data/processed/test_data.csv', index=False)
    
    # Save the scaler
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')
    print('Feature engineering completed and data saved.')

if __name__ == '__main__':
    engineer_features()
