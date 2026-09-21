import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# Load dataset
data_file = "../data/vessel_voyage_data.csv"
df = pd.read_csv(data_file)

# Features used for prediction
features = [
    "weather_condition",
    "port_stay_hours",
    "distance_nm",
    "avg_speed_knots",
    "engine_load_percent",
    "vessel_type"
]

target = "delay_hours"

X = df[features]
y = df[target]

# Categorical and numerical columns
categorical_features = [
    "weather_condition",
    "vessel_type"
]

numerical_features = [
    "port_stay_hours",
    "distance_nm",
    "avg_speed_knots",
    "engine_load_percent"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numerical",
            "passthrough",
            numerical_features
        )
    ]
)

# Machine learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Complete pipeline
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
pipeline.fit(X_train, y_train)

# Test model
predictions = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Delay prediction model training completed.")
print(f"Mean Absolute Error: {mae:.2f} hours")

# Predict delay for all voyages
df["predicted_delay_hours"] = pipeline.predict(X)

# Save predictions
output_file = "../data/delay_predictions.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"Prediction file created: {output_file}")
print(f"Total predictions: {len(df)}")