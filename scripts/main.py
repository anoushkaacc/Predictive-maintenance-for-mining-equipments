# scripts/main.py

import logging
from datetime import datetime
from data_preprocessing import preprocess_data
from feature_engineering import feature_engineering
from model_training import train_model
from model_evaluation import evaluate_model

# Set up logging
log_file = r'C:\Users\anoushka chatterjee\Desktop\project\logs\project.log'
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the predictive maintenance project")

    try:
        logging.info("Starting data preprocessing")
        preprocess_data()
        logging.info("Data preprocessing completed")

        logging.info("Starting feature engineering")
        feature_engineering()
        logging.info("Feature engineering completed")

        logging.info("Starting model training")
        train_model()
        logging.info("Model training completed")

        logging.info("Starting model evaluation")
        evaluate_model()
        logging.info("Model evaluation completed")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
