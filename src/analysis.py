def analyze_data(df):
    print("Columns:")
    print(df.columns)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nBasic Statistics:")
    print(df.describe())

    average_consumption = df["Water_Consumption_Liters"].mean()
    print("\nAverage Water Consumption:", average_consumption)

    print("\nMaximum Water Pressure Bar:", df["Water_Pressure_Bar"].max())