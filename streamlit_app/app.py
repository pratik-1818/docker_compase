# streamlit_app/app.py
import streamlit as st
import requests

st.title("🏡 House Price Prediction App")

st.sidebar.header("Enter House Features:")
MedInc = st.sidebar.number_input("Median Income", min_value=0.0, value=5.0)
HouseAge = st.sidebar.number_input("House Age", min_value=0.0, value=15.0)
AveRooms = st.sidebar.number_input("Average Rooms", min_value=0.0, value=5.0)
AveBedrms = st.sidebar.number_input("Average Bedrooms", min_value=0.0, value=1.0)
Population = st.sidebar.number_input("Population", min_value=0.0, value=1000.0)
AveOccup = st.sidebar.number_input("Average Occupancy", min_value=0.0, value=3.0)
Latitude = st.sidebar.number_input("Latitude", value=34.0)
Longitude = st.sidebar.number_input("Longitude", value=-118.0)

if st.button("Predict"):
    input_data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude,
    }
    try:
        response = requests.post("http://fastapi:8000/predict", json=input_data)
        result = response.json()
        st.success(f"💰 Predicted Price: {result['predicted_price (in 100,000s USD)']} x 100,000 USD")
    except:
        st.error("❌ Unable to connect to FastAPI backend.")
