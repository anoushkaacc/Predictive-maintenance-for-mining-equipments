# app.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd
from utils.data_loader import load_processed_data

# Initialize the Flask app
app = Flask(__name__)

# Load the model
model = joblib.load(r'C:\Users\anoushka chatterjee\Desktop\project\models\random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data from the request
    df = pd.DataFrame(data)  # Convert JSON to DataFrame
    predictions = model.predict(df)  # Make predictions
    return jsonify(predictions.tolist())  # Return predictions as JSON

if __name__ == '__main__':
    app.run(debug=True)
