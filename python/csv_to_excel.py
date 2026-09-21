import pandas as pd
from pathlib import Path

project_folder = Path(__file__).parent.parent

csv_file = project_folder / "data" / "vessel_voyage_data.csv"
excel_file = project_folder / "excel" / "Vessel_Performance_Analytics.xlsx"

df = pd.read_csv(csv_file)

df.to_excel(excel_file, index=False)

print("Excel file created successfully!")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {excel_file}")