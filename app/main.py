# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def read_root():
    return {"message": "Welcome to House Price Prediction API"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = np.array([[features.MedInc, features.HouseAge, features.AveRooms,
                            features.AveBedrms, features.Population,
                            features.AveOccup, features.Latitude, features.Longitude]])
    prediction = model.predict(input_data)[0]
    return {"predicted_price (in 100,000s USD)": round(prediction, 2)}
