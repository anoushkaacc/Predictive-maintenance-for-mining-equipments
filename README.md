# Predictive Maintenance for Mining Equipment

## Project overview
This project focuses on implementing a predictive maintenance system for mining equipment. By leveraging historical data, the model predicts potential failures before they occur, enabling proactive maintenance, reducing downtime, and improving operational efficiency.

## Predictive maintenance
Predictive maintenance involves using data analysis tools and techniques to detect anomalies in your operation and possible defects in equipment and processes so you can fix them before they result in failure. The goal is to predict when equipment failure might occur, and to prevent the occurrence of the failure by performing maintenance.

## Project structure:


### Description of Each Directory and File

- **data/**: Contains all the data used in the project.
  - **raw/**: Raw data files.
    - `equipment_data.csv`: The main dataset used for analysis.
  - **processed/**: Processed data files.
    - `train_data.csv`: Training dataset.
    - `test_data.csv`: Testing dataset.
    - `scaler.pkl`: Scaler object used for data normalization.
  - **external/**: External data sources.
    - `external_data_source.csv`: Additional data used for analysis.

- **notebooks/**: Jupyter notebooks for exploratory data analysis and feature engineering.
  - `eda.ipynb`: Notebook for exploratory data analysis.
  - `feature_engineering.ipynb`: Notebook for feature engineering.

- **scripts/**: Python scripts for various stages of the project.
  - `__init__.py`: Initialization file for the scripts module.
  - `data_preprocessing.py`: Script for data preprocessing.
  - `feature_engineering.py`: Script for feature engineering.
  - `model_training.py`: Script for training the predictive model.
  - `model_evaluation.py`: Script for evaluating the model.
  - `main.py`: Main script to run the entire pipeline.

- **models/**: Directory to save trained models.
  - `random_forest_model.pkl`: Trained Random Forest model.

- **reports/**: Directory for storing reports.
  - `evaluation_report.txt`: Report on model evaluation.

- **logs/**: Directory for storing log files.
  - [`project.log`](command:_github.copilot.openSymbolFromReferences?%5B%22project.log%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Canoushka%20chatterjee%5C%5CDesktop%5C%5Cproject%5C%5CREADME.md%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fanoushka%2520chatterjee%2FDesktop%2Fproject%2FREADME.md%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanoushka%20chatterjee%2FDesktop%2Fproject%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition"): Log file for tracking project execution.

- **utils/**: Utility scripts for data loading and saving.
  - `__init__.py`: Initialization file for the utils module.
  - `data_loader.py`: Script for loading data.
  - `data_saver.py`: Script for saving data.

- **requirements.txt**: List of dependencies required to run the project.
- **README.md**: This README file.
- **.gitignore**: Git ignore file to exclude unnecessary files from version control.

## Usage
- Data Preprocessing: Clean and preprocess the data.
- Exploratory Data Analysis (EDA): Visualize and understand the data.
- Feature Engineering: Create features for model training.
- Model Training: Train the predictive maintenance model.
- Model Evaluation: Evaluate the model's performance.
- Prediction: Use the model to predict potential failures.

## Running the project 

1. Fork this and Clone your repo

2. install the requirements
```bash
pip install -r requirements.txt
```
3. jupyter notebook for Exploratory data analysis
```bash
jupyter notebook notebooks/eda.ipynb
```
4. train the model
```bash
python scripts/model_training.py
```
5. evaluate the model
```bash
python scripts/model_evaluation.py
```
6. make predictions
```bash
python scripts/main.py
```
## Results

The model used for predictive maintenance is a Random forest classifier. Random forest is chosen due to its robustness and ability to handle large datasets with high dimensionality. 
The model's performance is evaluated using metrics such as accuracy, precision, recall, and F1 score. The results indicate that the model cam effectively predict potential failures, enabling proactive maintenance.

## Acknowledgements

This project was developed as part of internship training project under Southern Eastern CoalFields (SECL).