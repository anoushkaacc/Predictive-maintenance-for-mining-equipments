# model_evaluation.py

import pandas as pd
from sklearn.metrics import classification_report
import joblib
import os

def evaluate_model():
    # Load test data
    test_data_path = os.path.join('data', 'processed', 'test_data.csv')
    test_data = pd.read_csv(test_data_path)

    # Extract features and target
    X_test = test_data.drop(columns=['failure'])
    y_test = test_data['failure']

    # Load the trained model
    model_path = os.path.join('models', 'random_forest_model.pkl')
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    report = classification_report(y_test, y_pred)
    print(report)

    # Save the evaluation report
    report_path = os.path.join('reports', 'evaluation_report.txt')
    with open(report_path, 'w') as f:
        f.write(report)

    print(f"Evaluation report saved to {report_path}")

if __name__ == "__main__":
    evaluate_model()
