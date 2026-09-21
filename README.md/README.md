# AI-Powered Vessel Performance & Fuel Analytics Dashboard

An end-to-end data analytics project for analyzing vessel performance, voyage operations, fuel consumption, engine behavior, weather conditions, port activity, and voyage delays using Python, Excel, MySQL, Power BI, and Machine Learning.

## Project Overview

This project analyzes a large synthetic maritime dataset containing **100,000 vessel voyage records**.

The complete workflow is:

**Python → Excel → SQL/MySQL → Power BI → Machine Learning → GitHub**

## Business Questions

- How many voyages were analyzed?
- What is the total distance traveled?
- How much fuel was consumed?
- What is the average fuel efficiency?
- Which vessel types consume more fuel?
- How does vessel speed affect fuel consumption?
- How does engine load affect fuel consumption?
- How does weather affect fuel consumption?
- Which ports have higher delays?
- What factors contribute to voyage delays?
- Can fuel consumption be predicted?
- Can voyage delays be predicted?

## Dataset

The dataset contains **100,000 voyage records** with:

- Voyage ID
- Vessel ID
- Vessel Type
- Departure Port
- Arrival Port
- Distance (NM)
- Average Speed (Knots)
- Engine Power (kW)
- Engine Load (%)
- Engine RPM
- Fuel Consumption (Tons)
- Fuel Efficiency
- Weather Condition
- Wind Speed (Knots)
- Wave Height (m)
- Temperature (°C)
- Port Stay Hours
- Voyage Duration (Hours)
- Delay Hours

## Project Structure

```text
Vessel_Performance_Analytics
│
├── ai
│   ├── fuel_prediction.py
│   └── delay_prediction.py
│
├── data
│   ├── vessel_voyage_data.csv
│   ├── fuel_predictions.csv
│   └── delay_predictions.csv
│
├── excel
│   └── Vessel_Performance_Analytics.xlsx
│
├── powerbi
│   └── Power BI dashboard files
│
├── python
│   ├── generate_data.py
│   └── csv_to_excel.py
│
└── sql
    └── vessel_analysis.sql
## Technologies Used

- Python
- Pandas
- NumPy
- Faker
- Matplotlib
- Seaborn
- Scikit-learn
- Excel
- MySQL
- SQL
- Power BI
- Git
- GitHub

## Python Data Generation

Python was used to generate the synthetic maritime dataset containing **100,000 voyage records**.

Generated dataset:

`data/vessel_voyage_data.csv`

## Excel Analysis

Excel was used for:

- Data storage
- KPI calculations
- Data analysis
- Vessel type analysis
- Port analysis
- Weather analysis
- Charts and visualizations

### Main KPIs

- Total Voyages
- Total Distance
- Total Fuel Consumed
- Average Speed
- Average Fuel Efficiency
- Average Delay

## SQL Analysis

MySQL was used for business-oriented analysis including:

- Voyage counts
- Vessel type analysis
- Average speed
- Average fuel consumption
- Fuel efficiency
- Engine load
- Voyage delays

SQL queries:

`sql/vessel_analysis.sql`

## Machine Learning

Two machine learning models were developed.

### Fuel Consumption Prediction

The model predicts fuel consumption using factors such as:

- Distance
- Speed
- Engine Load
- Engine Power
- Weather
- Vessel Type
- Wave Height
- Wind Speed

**Model:** Random Forest Regression

Output:

`data/fuel_predictions.csv`

### Voyage Delay Prediction

The model predicts voyage delay using factors such as:

- Weather
- Port Stay
- Distance
- Vessel information
- Voyage information
- Environmental conditions

**Model:** Random Forest Regression

Output:

`data/delay_predictions.csv`

## Power BI Dashboard
![Power BI Dashboard](images/powerbi-dashboard.png)

The Power BI dashboard provides an interactive view of vessel performance and operational data.

### Dashboard KPIs

- Total Voyages
- Total Distance
- Total Fuel Consumed
- Average Fuel per NM
- Average Speed
- Average Delay
- Fuel Cost
- Vessel Performance

### Dashboard Analysis

- Vessel Performance
- Fuel Consumption
- Vessel Types
- Departure Ports
- Weather Conditions
- Engine Performance
- Voyage Delays
- AI Predicted Fuel Consumption
- AI Predicted Voyage Delay

## AI Integration

Machine learning predictions were integrated into the analytics workflow.

The dashboard includes:

- AI Predicted Fuel Consumption
- AI Predicted Voyage Delay

This combines traditional business intelligence with predictive analytics.

## Project Workflow

```text
Raw Data
   ↓
Python Data Generation
   ↓
Data Cleaning & Analysis
   ↓
Excel Analysis
   ↓
SQL / MySQL Analysis
   ↓
Power BI Dashboard
   ↓
Machine Learning
   ↓
AI Predictions
   ↓
Power BI AI Insights
   ↓
Business Insights
## Key Skills Demonstrated

- Data Generation
- Data Cleaning
- Exploratory Data Analysis
- SQL Querying
- Excel Analysis
- KPI Development
- Data Visualization
- Power BI Dashboard Development
- Machine Learning
- Predictive Analytics
- Business Analysis
- Git & GitHub

## Author

**Aathish GP**

B.E. Computer Science and Engineering

Tamil Nadu, India

GitHub: https://github.com/aathishgp777

LinkedIn: https://www.linkedin.com/in/aathish-gp-68a75a379/