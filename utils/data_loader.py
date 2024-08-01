import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)

def load_processed_data():
    """
    Load the processed training and test data.
    
    Returns:
    tuple: X_train, X_test, y_train, y_test
    """
    X_train = load_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\train_data.csv')
    X_test = load_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\test_data.csv')
    y_train = load_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\train_labels.csv').values.ravel()
    y_test = load_csv(r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\test_labels.csv').values.ravel()
    
    return X_train, X_test, y_train, y_test
