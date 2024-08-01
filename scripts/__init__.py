# scripts/__init__.py

# Importing modules from scripts package
from .data_preprocessing import preprocess_data, split_and_scale_data, save_processed_data
from .feature_engineering import create_features
from .model_training import train_model
from .model_evaluation import evaluate_model

# Defining package-level variables if necessary
PACKAGE_NAME = "predictive_maintenance_scripts"
