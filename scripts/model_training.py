import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

def load_data(train_data_path, train_labels_path):
    X_train = pd.read_csv(train_data_path)
    y_train = pd.read_csv(train_labels_path).values.ravel()  # Flatten the labels array
    return X_train, y_train

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, model_path):
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def main():
    train_data_path = r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\train_data.csv'
    train_labels_path = r'C:\Users\anoushka chatterjee\Desktop\project\data\processed\train_labels.csv'
    model_path = r'C:\Users\anoushka chatterjee\Desktop\project\models\random_forest_model.pkl'

    X_train, y_train = load_data(train_data_path, train_labels_path)
    model = train_model(X_train, y_train)
    save_model(model, model_path)

if __name__ == "__main__":
    main()
