import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Function to generate synthetic data
def generate_synthetic_data(start_date, end_date, freq='H'):
    # Create a date range
    date_range = pd.date_range(start=start_date, end=end_date, freq=freq)

    # Generate synthetic data
    temperature = np.random.normal(loc=75, scale=10, size=len(date_range))
    pressure = np.random.normal(loc=30, scale=5, size=len(date_range))
    vibration = np.random.normal(loc=0.02, scale=0.01, size=len(date_range))

    # Simulate failures based on some condition (e.g., high temperature or high vibration)
    failure = ((temperature > 85) | (vibration > 0.03)).astype(int)

    # Create a DataFrame
    data = pd.DataFrame({
        'timestamp': date_range,
        'temperature': temperature,
        'pressure': pressure,
        'vibration': vibration,
        'failure': failure
    })

    return data

# Define the date range for the synthetic data
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate the synthetic data
synthetic_data = generate_synthetic_data(start_date, end_date)

# Save to CSV
synthetic_data.to_csv('equipment_data.csv', index=False)

print("Synthetic data generated and saved to equipment_data.csv")
