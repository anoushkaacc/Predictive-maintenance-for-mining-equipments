import pandas as pd
import os

def load_data(file_path):
  data=pd.read_csv(file_path)
  return data