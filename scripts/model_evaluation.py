import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def load_data(test_data_path, test_labels_path):
    X_test = pd.read_csv(test_data_path)
    y_test = pd.read_csv(test_labels_path).values.ravel()  # Flatten the labels array
    return X_test, y_test

def load_model(model_path):
    return joblib.load(model_path)

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    
    return accuracy, conf_matrix, class_report

def save_evaluation_report(accuracy, conf_matrix, class_report, report_path):
    with open(report_path, 'w') as f:
        f.write(f"Accuracy: {accuracy}\n")
        f.write(f"Confusion Matrix:\n{conf_matrix}\n")
        f.write(f"Classification Report:\n{class_report}\n")
    print(f"Evaluation report saved to {report_path}")

def main():
    test_data_path = r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\test_data.csv'
    test_labels_path = r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\test_labels.csv'
    model_path = r'C:\Users\anoushka chatterjee\Desktop\project\models\random_forest_model.pkl'
    report_path = r'C:\Users\anoushka chatterjee\Desktop\project\reports\evaluation_report.txt'

    X_test, y_test = load_data(test_data_path, test_labels_path)
    model = load_model(model_path)
    accuracy, conf_matrix, class_report = evaluate_model(model, X_test, y_test)
    save_evaluation_report(accuracy, conf_matrix, class_report, report_path)

if __name__ == "__main__":
    main()
