import plotly.express as px



def create_anomaly_chart(df):
    df = df.copy()

    df["Anomaly"] = df["Anomaly"].astype(str).map({
        "1": "Water Usage",
        "-1": "Water Leakage"
    })

    chart = px.scatter(
        df,
        x="Date",
        y="Water_Consumption_Liters",
        color="Anomaly",
        hover_data=["Time", "Flow_Rate_LPM", "Water_Pressure_Bar"],
        labels={
            "Water_Consumption_Liters": "Water Consumption (Liters)",
            "Date": "Date",
            "Anomaly": "Detection Result"
        },
        color_discrete_map={
            "Water Usage": "blue",
            "Water Leakage": "red"
        }
    )
    return chart



def create_flow_chart(df):
    chart = px.line(
        df,
        x="Date",
        y="Flow_Rate_LPM",
        title="Water Flow Rate Over Time",
        markers=True,
        labels={
                    "Date": "Date",
                    "Flow_Rate_LPM": "Flow Rate (L/min)"
                }
    )

    return chart



def create_pressure_chart(df):
    chart = px.line(
        df,
        x="Date",
        y="Water_Pressure_Bar",
        title="Water Pressure Over Time",
        markers=True,
        labels={
            "Date": "Date",
            "Water_Pressure_Bar": "Water Pressure (Bar)"
        }
    )

    return chart
