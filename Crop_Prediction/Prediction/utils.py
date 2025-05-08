import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_models/model.pkl')

# Load model once when server starts
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def predict_result(features_list):
    return model.predict([features_list])[0]
