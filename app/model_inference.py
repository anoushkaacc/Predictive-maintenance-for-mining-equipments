import joblib
import pandas as pd
import os

def load_model(model_path):
  model=joblib.load(model_path)
  return model
def make_predeictions(model, data):
  predictions = model.predict(data)
  return predictions