import pandas as pd
import joblib

def save_csv(df, file_path):
    """
    Save a pandas DataFrame to a CSV file.
    
    Parameters:
    df (pd.DataFrame): DataFrame to be saved.
    file_path (str): Path to the CSV file.
    """
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

def save_model(model, model_path):
    """
    Save a machine learning model to a file.
    
    Parameters:
    model (object): Trained model to be saved.
    model_path (str): Path to the file where the model will be saved.
    """
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def save_evaluation_report(accuracy, conf_matrix, class_report, report_path):
    """
    Save the evaluation report to a text file.
    
    Parameters:
    accuracy (float): Accuracy score of the model.
    conf_matrix (ndarray): Confusion matrix of the model.
    class_report (str): Classification report of the model.
    report_path (str): Path to the text file where the report will be saved.
    """
    with open(report_path, 'w') as f:
        f.write(f"Accuracy: {accuracy}\n")
        f.write(f"Confusion Matrix:\n{conf_matrix}\n")
        f.write(f"Classification Report:\n{class_report}\n")
    print(f"Evaluation report saved to {report_path}")
