from src.analysis import *
from src.preprocessing import *
from src.ml_model import *
from src.visualization import *
import streamlit as st
import os

df = load_data("data/water_consumption_dataset.csv")
df=clean_data(df)

st.title("Smart Water Monitoring & Leakage Detection")

st.subheader("Water Consumption Data")
st.dataframe(df)
analyze_data(df)

features = create_features(df)

model_path = "water_anomaly_model.pkl"

if os.path.exists(model_path):
    model = load_model()
else:
    model = train_model(features)
    save_model(model)

predictions = detect_anomalies(model, features)


df["Anomaly"] = predictions


normal_count = (df["Anomaly"] == 1).sum()
anomaly_count = (df["Anomaly"] == -1).sum()


st.subheader("Dashboard Overview")

total_consumption = df["Water_Consumption_Liters"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Water Consumption", f"{total_consumption:.2f} L")
col2.metric("Normal Readings", normal_count)
col3.metric("Anomalies Detected", anomaly_count)

anomaly_percentage = (anomaly_count / len(df)) * 100

st.subheader("Anomaly Percentage")
st.metric("Anomalies (%)", f"{anomaly_percentage:.2f}%")

anomalies = df[predictions== -1]

anomalies = anomalies.sort_values(by=["Date", "Time"])

st.subheader("Detected Anomalies")
st.dataframe(anomalies)

st.subheader("Water Usage & Leakage Detection")
chart = create_anomaly_chart(df)
st.plotly_chart(chart, use_container_width=True)


st.subheader("Water Flow Rate")
flow_chart = create_flow_chart(df)
st.plotly_chart(flow_chart)

st.subheader("Water Pressure")
pressure_chart = create_pressure_chart(df)
st.plotly_chart(pressure_chart)


st.subheader("Leakage Alert")

if anomaly_count > 0:
    st.error(f"{anomaly_count} unusual readings detected!")
    st.write("Possible leakage or unusual water usage. Please inspect the readings.")
else:
    st.success("No unusual readings detected.")



st.subheader("Predict New Water Reading")

consumption = st.number_input(
    "Water Consumption (Liters)",
    min_value=0.0,
    value=10.0
)

flow_rate = st.number_input(
    "Flow Rate (L/min)",
    min_value=0.0,
    value=2.0
)

pressure = st.number_input(
    "Water Pressure (Bar)",
    min_value=0.0,
    value=2.5
)

hour = st.number_input(
    "Hour (0-23)",
    min_value=0,
    max_value=23,
    value=12
)

if st.button("Predict"):
    result = predict_new_reading(
        model,
        consumption,
        flow_rate,
        pressure,
        hour
    )

    if result == "Normal Reading":
        st.success(result)
    else:
        st.error(result)
