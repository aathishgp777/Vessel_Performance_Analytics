-- ============================================================
-- AI-Powered Vessel Performance & Fuel Analytics
-- SQL Analysis
-- Database: vessel_analytics
-- Table: vessel_data
-- ============================================================

USE vessel_analytics;


-- ============================================================
-- STEP 1: View Sample Data
-- ============================================================

SELECT *
FROM vessel_analytics.vessel_data
LIMIT 10;


-- ============================================================
-- STEP 2: Check Total Records
-- ============================================================

SELECT COUNT(*) AS total_rows
FROM vessel_analytics.vessel_data;


-- ============================================================
-- STEP 3: Voyage Count by Vessel Type
-- ============================================================

SELECT
    vessel_type,
    COUNT(*) AS total_voyages
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY total_voyages DESC;


-- ============================================================
-- STEP 4: Average Speed by Vessel Type
-- ============================================================

SELECT
    vessel_type,
    ROUND(AVG(avg_speed_knots), 2) AS average_speed
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY average_speed DESC;


-- ============================================================
-- STEP 5: Average Fuel Consumption by Vessel Type
-- ============================================================

SELECT
    vessel_type,
    ROUND(AVG(fuel_consumption_tons), 2) AS avg_fuel_consumption
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY avg_fuel_consumption DESC;


-- ============================================================
-- STEP 6: Average Fuel Efficiency by Vessel Type
-- ============================================================

SELECT
    vessel_type,
    ROUND(AVG(fuel_efficiency), 2) AS avg_fuel_efficiency
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY avg_fuel_efficiency DESC;


-- ============================================================
-- STEP 7: Average Engine Load by Vessel Type
-- ============================================================

SELECT
    vessel_type,
    ROUND(AVG(engine_load_percent), 2) AS avg_engine_load
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY avg_engine_load DESC;


-- ============================================================
-- STEP 8: Average Delay by Vessel Type
-- ============================================================

SELECT
    vessel_type,
    ROUND(AVG(delay_hours), 2) AS avg_delay_hours
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY avg_delay_hours DESC;


-- ============================================================
-- STEP 9: Port Analysis
-- ============================================================

SELECT
    departure_port,
    COUNT(*) AS total_voyages,
    ROUND(AVG(distance_nm), 2) AS avg_distance_nm,
    ROUND(AVG(fuel_consumption_tons), 2) AS avg_fuel_consumption,
    ROUND(AVG(delay_hours), 2) AS avg_delay_hours
FROM vessel_analytics.vessel_data
GROUP BY departure_port
ORDER BY total_voyages DESC;


-- ============================================================
-- STEP 10: Weather Impact Analysis
-- ============================================================

SELECT
    weather_condition,
    COUNT(*) AS total_voyages,
    ROUND(AVG(fuel_consumption_tons), 2) AS avg_fuel_consumption,
    ROUND(AVG(fuel_efficiency), 2) AS avg_fuel_efficiency,
    ROUND(AVG(delay_hours), 2) AS avg_delay_hours,
    ROUND(AVG(wind_speed_knots), 2) AS avg_wind_speed
FROM vessel_analytics.vessel_data
GROUP BY weather_condition
ORDER BY avg_fuel_consumption DESC;


-- ============================================================
-- STEP 11: Distance vs Fuel Consumption
-- ============================================================

SELECT
    vessel_type,
    ROUND(AVG(distance_nm), 2) AS avg_distance_nm,
    ROUND(AVG(fuel_consumption_tons), 2) AS avg_fuel_consumption,
    ROUND(
        AVG(fuel_consumption_tons / NULLIF(distance_nm, 0)),
        4
    ) AS fuel_per_nm
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY fuel_per_nm DESC;


-- ============================================================
-- STEP 12: Engine Performance
-- ============================================================

SELECT
    vessel_type,
    ROUND(AVG(engine_power_kw), 2) AS avg_engine_power_kw,
    ROUND(AVG(engine_load_percent), 2) AS avg_engine_load,
    ROUND(AVG(engine_rpm), 2) AS avg_engine_rpm,
    ROUND(AVG(fuel_consumption_tons), 2) AS avg_fuel_consumption
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY avg_fuel_consumption DESC;


-- ============================================================
-- STEP 13: Top 20 High-Delay Voyages
-- ============================================================

SELECT
    voyage_id,
    vessel_id,
    vessel_type,
    departure_port,
    arrival_port,
    distance_nm,
    weather_condition,
    delay_hours
FROM vessel_analytics.vessel_data
ORDER BY delay_hours DESC
LIMIT 20;


-- ============================================================
-- STEP 14: Top 20 High-Fuel-Consumption Voyages
-- ============================================================

SELECT
    voyage_id,
    vessel_id,
    vessel_type,
    departure_port,
    arrival_port,
    distance_nm,
    avg_speed_knots,
    engine_load_percent,
    weather_condition,
    fuel_consumption_tons
FROM vessel_analytics.vessel_data
ORDER BY fuel_consumption_tons DESC
LIMIT 20;


-- ============================================================
-- STEP 15: Final Vessel Performance Summary
-- ============================================================

SELECT
    vessel_type,
    COUNT(*) AS total_voyages,
    ROUND(AVG(distance_nm), 2) AS avg_distance_nm,
    ROUND(AVG(avg_speed_knots), 2) AS avg_speed_knots,
    ROUND(AVG(fuel_consumption_tons), 2) AS avg_fuel_consumption,
    ROUND(AVG(fuel_efficiency), 2) AS avg_fuel_efficiency,
    ROUND(AVG(engine_load_percent), 2) AS avg_engine_load,
    ROUND(AVG(delay_hours), 2) AS avg_delay_hours
FROM vessel_analytics.vessel_data
GROUP BY vessel_type
ORDER BY avg_fuel_efficiency DESC;


-- ============================================================
-- SQL ANALYSIS COMPLETE
-- ============================================================