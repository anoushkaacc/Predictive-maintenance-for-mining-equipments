# model_training.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

def train_model():
    # Load training data
    train_data_path = os.path.join('data', 'processed', 'train_data.csv')
    train_data = pd.read_csv(train_data_path)

    # Extract features and target
    X_train = train_data.drop(columns=['failure'])
    y_train = train_data['failure']

    # Train the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    model_path = os.path.join('models', 'random_forest_model.pkl')
    joblib.dump(model, model_path)

    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    train_model()
