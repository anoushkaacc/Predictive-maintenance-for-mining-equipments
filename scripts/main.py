
# main.py

import logging
import os
from data_preprocessing import preprocess_data
from feature_engineering import engineer_features
from model_training import train_model
from model_evaluation import evaluate_model

# Set up logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/project.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    try:
        logging.info('Starting data preprocessing')
        preprocess_data()
        logging.info('Data preprocessing completed')

        logging.info('Starting feature engineering')
        engineer_features()
        logging.info('Feature engineering completed')

        logging.info('Starting model training')
        train_model()
        logging.info('Model training completed')

        logging.info('Starting model evaluation')
        evaluate_model()
        logging.info('Model evaluation completed')

        logging.info('Project execution completed successfully')

    except Exception as e:
        logging.error(f'Error during project execution: {e}', exc_info=True)

if __name__ == '__main__':
    main()
