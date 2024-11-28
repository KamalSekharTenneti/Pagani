# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data =pd .read_csv('Pagani.csv')
df = pd.DataFrame(data)

# Encode categorical columns
label_encoders = {}
for col in ["Model", "FuelType"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define features and targets
X = df[["Year", "Model", "FuelType"]]
y_units = df["UnitsSold"]
y_price = df["AvgPriceUSD"]
y_satisfaction = df["CustomerSatisfaction"]

# Train-test split
X_train, X_test, y_units_train, y_units_test = train_test_split(X, y_units, test_size=0.2, random_state=42)
X_train, X_test, y_price_train, y_price_test = train_test_split(X, y_price, test_size=0.2, random_state=42)
X_train, X_test, y_satisfaction_train, y_satisfaction_test = train_test_split(X, y_satisfaction, test_size=0.2, random_state=42)

# Initialize and train models
model_units = RandomForestRegressor(random_state=42)
model_price = RandomForestRegressor(random_state=42)
model_satisfaction = RandomForestRegressor(random_state=42)

model_units.fit(X_train, y_units_train)
model_price.fit(X_train, y_price_train)
model_satisfaction.fit(X_train, y_satisfaction_train)

# Predict for 2025
future_data = pd.DataFrame({
    "Year": [2025, 2025, 2025],
    "Model": label_encoders["Model"].transform(["Pagani EV1", "Pagani Diesel1", "Pagani Petrol1"]),
    "FuelType": label_encoders["FuelType"].transform(["Electric", "Diesel", "Petrol"])
})

predicted_units = model_units.predict(future_data)
predicted_price = model_price.predict(future_data)
predicted_satisfaction = model_satisfaction.predict(future_data)

# Combine predictions into a DataFrame
predictions_2025 = future_data.copy()
predictions_2025["UnitsSold"] = predicted_units
predictions_2025["AvgPriceUSD"] = predicted_price
predictions_2025["CustomerSatisfaction"] = predicted_satisfaction

# Decode categorical values for better readability
predictions_2025["Model"] = label_encoders["Model"].inverse_transform(predictions_2025["Model"])
predictions_2025["FuelType"] = label_encoders["FuelType"].inverse_transform(predictions_2025["FuelType"])

print(predictions_2025)
