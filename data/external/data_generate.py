import pandas as pd
import numpy as np

# Define the number of records
num_records = 1000

# Generate synthetic data
np.random.seed(0)
timestamp = pd.date_range(start='2023-01-01', periods=num_records, freq='H')
temperature = np.random.normal(loc=70, scale=10, size=num_records)
pressure = np.random.normal(loc=30, scale=5, size=num_records)
vibration = np.random.normal(loc=5, scale=1, size=num_records)

# Create a DataFrame
external_df = pd.DataFrame({
    'timestamp': timestamp,
    'temperature': temperature,
    'pressure': pressure,
    'vibration': vibration
})

# Save to CSV
external_data_path = r'C:\Users\anoushka chatterjee\Desktop\project\data\external\external_data_source.csv'
external_df.to_csv(external_data_path, index=False)
print(f"External data saved to {external_data_path}")
