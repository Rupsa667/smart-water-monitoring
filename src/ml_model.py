import pandas as pd
import joblib as jb
from sklearn.ensemble import IsolationForest

def create_features(df):
    df["Hour"] = pd.to_datetime(df["Time"]).dt.hour

    features = df[
        [
            "Water_Consumption_Liters",
            "Flow_Rate_LPM",
            "Water_Pressure_Bar",
            "Hour"
        ]
    ]

    return features

def train_model(features):
    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    model.fit(features)

    return model

def detect_anomalies(model, features):
    predictions = model.predict(features)

    return predictions


def save_model(model):
    jb.dump(model, "water_anomaly_model.pkl")


def load_model():
    return jb.load("water_anomaly_model.pkl")


def predict_new_reading(model, consumption, flow_rate, pressure, hour):
    new_data = [[consumption, flow_rate, pressure, hour]]

    prediction = model.predict(new_data)

    if prediction[0] == 1:
        return "Normal Reading"
    else:
        return "Anomaly Detected"
