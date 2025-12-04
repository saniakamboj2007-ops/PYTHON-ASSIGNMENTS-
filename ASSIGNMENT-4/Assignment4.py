# -------------------------------------------
# WEATHER DATA VISUALIZER – FIXED VERSION
# Using: weatherHistory.csv
# -------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# TASK 1: Load the CSV File
# -----------------------------
df = pd.read_csv("weatherHistory.csv")

print("Head of Dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# -----------------------------
# TASK 2: Data Cleaning
# -----------------------------

# Convert 'Formatted Date' to datetime
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True, errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Formatted Date'])

# Set Datetime as index (required for resample)
df = df.set_index('Formatted Date')

# Rename columns (clean names)
df = df.rename(columns={
    'Temperature (C)': 'Temperature',
    'Apparent Temperature (C)': 'FeelsLike',
    'Wind Speed (km/h)': 'WindSpeed'
})

# Handle missing numeric values
numeric_cols = ['Temperature', 'Humidity', 'WindSpeed']
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mean())

print("\nCleaned DataFrame Info:")
print(df.info())

# -----------------------------
# TASK 3: Statistical Analysis
# -----------------------------

print("\n--- Daily Statistics ---")
daily_stats = df['Temperature'].resample('D').agg(['mean', 'min', 'max', 'std'])
print(daily_stats.head())

print("\n--- Monthly Statistics ---")
monthly_stats = df['Temperature'].resample('M').agg(['mean', 'min', 'max', 'std'])
print(monthly_stats.head())


# -----------------------------
# TASK 4: Visualization
# -----------------------------

# 1. Line chart – Daily Temperature Trend
plt.figure(figsize=(12,5))
plt.plot(df.index, df['Temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("daily_temperature_trend.png")
plt.close()


# 2. Bar Chart – Monthly Average Humidity
if "Humidity" in df.columns:
    monthly_humidity = df['Humidity'].resample('M').mean()

    plt.figure(figsize=(12,5))
    monthly_humidity.plot(kind='bar')
    plt.title("Average Monthly Humidity")
    plt.xlabel("Month")
    plt.ylabel("Humidity")
    plt.savefig("monthly_humidity_bar.png")
    plt.close()


# 3. Scatter Plot – Humidity vs Temperature
plt.figure(figsize=(8,5))
plt.scatter(df['Temperature'], df['Humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity")
plt.grid(True)
plt.savefig("humidity_vs_temperature.png")
plt.close()


# -----------------------------
# TASK 5: Grouping & Aggregation
# -----------------------------

df['Month'] = df.index.month
df['Year'] = df.index.year

monthly_group = df.groupby('Month')['Temperature'].mean()
yearly_group = df.groupby('Year')['Temperature'].mean()

print("\nAverage Temperature by Month:")
print(monthly_group)

print("\nAverage Temperature by Year:")
print(yearly_group)


# -----------------------------
# TASK 6: Export Cleaned Data
# -----------------------------
df.to_csv("cleaned_weather_history.csv")
print("\nCleaned data exported successfully!")

print("\nAll required charts saved as PNG files.")

