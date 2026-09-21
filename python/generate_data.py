import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

fake = Faker()
np.random.seed(42)

TOTAL_RECORDS = 100000

vessel_types = [
    "Container Ship",
    "Bulk Carrier",
    "Oil Tanker",
    "LNG Carrier",
    "Ro-Ro Ship",
    "General Cargo"
]

weather_conditions = [
    "Clear",
    "Cloudy",
    "Rain",
    "Storm",
    "Fog"
]

ports = [
    "Singapore",
    "Rotterdam",
    "Shanghai",
    "Dubai",
    "Colombo",
    "Mumbai",
    "Chennai",
    "Hamburg",
    "Los Angeles",
    "Busan"
]

vessel_ids = [f"VESSEL_{i:05d}" for i in range(1, 1001)]

data = []

for i in range(TOTAL_RECORDS):

    vessel_id = np.random.choice(vessel_ids)
    vessel_type = np.random.choice(vessel_types)

    departure_port = np.random.choice(ports)
    arrival_port = np.random.choice(
        [port for port in ports if port != departure_port]
    )

    distance_nm = round(np.random.uniform(100, 12000), 2)
    avg_speed_knots = round(np.random.uniform(8, 25), 2)

    engine_power_kw = np.random.randint(5000, 60000)
    engine_load_percent = round(np.random.uniform(40, 100), 2)
    engine_rpm = round(np.random.uniform(60, 180), 2)

    fuel_consumption_tons = round(
        distance_nm *
        (0.015 + engine_load_percent / 100000) *
        np.random.uniform(0.8, 1.3),
        2
    )

    weather = np.random.choice(weather_conditions)

    wind_speed_knots = round(np.random.uniform(2, 45), 2)
    wave_height_m = round(np.random.uniform(0.2, 8), 2)
    temperature_c = round(np.random.uniform(5, 35), 2)

    port_stay_hours = round(np.random.uniform(4, 72), 2)

    weather_delay = {
        "Clear": 0,
        "Cloudy": 2,
        "Rain": 5,
        "Storm": 15,
        "Fog": 10
    }

    delay_hours = round(
        max(
            0,
            np.random.normal(
                weather_delay[weather] + port_stay_hours / 20,
                5
            )
        ),
        2
    )

    voyage_duration_hours = round(
        (distance_nm / avg_speed_knots) + port_stay_hours,
        2
    )

    fuel_efficiency = round(
        fuel_consumption_tons / distance_nm,
        4
    )

    data.append([
        f"VOYAGE_{i + 1:06d}",
        vessel_id,
        vessel_type,
        departure_port,
        arrival_port,
        distance_nm,
        avg_speed_knots,
        engine_power_kw,
        engine_load_percent,
        engine_rpm,
        fuel_consumption_tons,
        fuel_efficiency,
        weather,
        wind_speed_knots,
        wave_height_m,
        temperature_c,
        port_stay_hours,
        voyage_duration_hours,
        delay_hours
    ])

columns = [
    "voyage_id",
    "vessel_id",
    "vessel_type",
    "departure_port",
    "arrival_port",
    "distance_nm",
    "avg_speed_knots",
    "engine_power_kw",
    "engine_load_percent",
    "engine_rpm",
    "fuel_consumption_tons",
    "fuel_efficiency",
    "weather_condition",
    "wind_speed_knots",
    "wave_height_m",
    "temperature_c",
    "port_stay_hours",
    "voyage_duration_hours",
    "delay_hours"
]

df = pd.DataFrame(data, columns=columns)

output_folder = Path(__file__).parent.parent / "data"
output_folder.mkdir(exist_ok=True)

csv_path = output_folder / "vessel_voyage_data.csv"

df.to_csv(csv_path, index=False)

print("Data generation completed!")
print(f"Total records: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {csv_path}")