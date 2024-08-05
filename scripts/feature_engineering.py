# feature_engineering.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

def engineer_features():
    # Load preprocessed data
    preprocessed_data_path = os.path.join('data', 'processed', 'preprocessed_data.csv')
    data = pd.read_csv(preprocessed_data_path)

    # Extract features and target
    features = data.drop(columns=['failure', 'timestamp'])
    target = data['failure']

    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Save the scaler for future use
    scaler_path = os.path.join('data', 'processed', 'scaler.pkl')
    joblib.dump(scaler, scaler_path)

    # Split data into training and test sets
    train_size = int(0.8 * len(data))
    train_features = scaled_features[:train_size]
    train_target = target[:train_size]
    test_features = scaled_features[train_size:]
    test_target = target[train_size:]

    # Save the processed data
    train_data = pd.DataFrame(train_features, columns=features.columns)
    train_data['failure'] = train_target.reset_index(drop=True)
    test_data = pd.DataFrame(test_features, columns=features.columns)
    test_data['failure'] = test_target.reset_index(drop=True)

    train_data_path = os.path.join('data', 'processed', 'train_data.csv')
    test_data_path = os.path.join('data', 'processed', 'test_data.csv')
    
    train_data.to_csv(train_data_path, index=False)
    test_data.to_csv(test_data_path, index=False)

    print(f"Train and test data saved to {train_data_path} and {test_data_path} respectively.")

if __name__ == "__main__":
    engineer_features()
