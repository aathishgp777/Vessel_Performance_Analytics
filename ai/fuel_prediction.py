import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error

# Load vessel dataset
df = pd.read_csv("../data/vessel_voyage_data.csv")

# Features used for prediction
features = [
    "distance_nm",
    "avg_speed_knots",
    "engine_load_percent",
    "vessel_type",
    "weather_condition"
]

target = "fuel_consumption_tons"

X = df[features]
y = df[target]

# Categorical columns
categorical_columns = [
    "vessel_type",
    "weather_condition"
]

# Numerical columns
numerical_columns = [
    "distance_nm",
    "avg_speed_knots",
    "engine_load_percent"
]

# Prepare data
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)

# Machine learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Complete ML pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
print("Training fuel prediction model...")
pipeline.fit(X_train, y_train)

# Test model
predictions = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Model training completed.")
print(f"Mean Absolute Error: {mae:.2f} tons")

# Predict fuel consumption for all voyages
df["predicted_fuel_consumption_tons"] = pipeline.predict(X)

# Save prediction results
output_file = "../data/fuel_predictions.csv"
df.to_csv(output_file, index=False)

print(f"Prediction file created: {output_file}")
print("Total predictions:", len(df))