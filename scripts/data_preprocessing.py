import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load the raw data
def load_raw_data(file_path):
    return pd.read_csv(file_path)

# Preprocess the data
def preprocess_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['temp_rolling_mean'] = df['temperature'].rolling(window=5).mean()
    df['pressure_rolling_mean'] = df['pressure'].rolling(window=5).mean()
    df['vibration_rolling_mean'] = df['vibration'].rolling(window=5).mean()
    df.dropna(inplace=True)
    return df

# Split the data into train and test sets
def split_and_scale_data(df):
    X = df[['temperature', 'pressure', 'vibration', 'temp_rolling_mean', 'pressure_rolling_mean', 'vibration_rolling_mean']]
    y = df['failure']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

# Save processed data
def save_processed_data(X_train, X_test, y_train, y_test, scaler):
    pd.DataFrame(X_train).to_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\train_data.csv', index=False)
    pd.DataFrame(X_test).to_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\test_data.csv', index=False)
    pd.DataFrame(y_train).to_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\train_labels.csv', index=False)
    pd.DataFrame(y_test).to_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\test_labels.csv', index=False)
    joblib.dump(scaler, r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\scaler.pkl')

# Main function to load, preprocess, split, scale, and save the data
def main():
    df = load_raw_data(r'C:\Users\anoushka chatterjee\Desktop\project\data\raw\equipment_data.csv')
    df = preprocess_data(df)
    X_train, X_test, y_train, y_test, scaler = split_and_scale_data(df)
    save_processed_data(X_train, X_test, y_train, y_test, scaler)

if __name__ == "__main__":
    main()
