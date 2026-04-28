# 🚦 Accident Risk Analysis Dashboard

An interactive **Streamlit-based Exploratory Data Analysis (EDA) dashboard** for analyzing road accident patterns, identifying high-risk zones, and visualizing accident severity using geospatial mapping and statistical insights.

---

## 📌 Project Overview

This project analyzes accident data in Kerala using interactive visualizations and maps. It helps in understanding:

- Accident hotspots
- Severity distribution
- Vehicle type involvement
- Alcohol and overspeeding impact
- Time-based accident trends

If no dataset is uploaded, the app automatically generates a **sample dataset** for demonstration.

---

## 🎯 Objectives

- Identify accident-prone areas in Kerala
- Analyze severity patterns and risk factors
- Provide interactive visual exploration of data
- Improve decision-making through data insights

---

## ⚡ Features

- 📂 Upload custom CSV dataset
- 🗺️ Interactive Heatmap (Folium)
- 🎛️ Dynamic sidebar filters
- 📅 Date range filtering
- 📊 Multiple charts (Line, Bar, Area)
- 📈 Statistical summary dashboard
- 📍 Geospatial accident visualization
- ⬇️ Download filtered dataset

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Folium
- Matplotlib
- Plotly
- Streamlit-Folium

---

## 📁 Dataset Format

Your CSV file should contain the following columns:

| Column | Description |
|--------|------------|
| Date | Accident date |
| City | Location / District |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |
| Accident_Severity | Low / Medium / High |
| Vehicle_Type | Car / Bike / Truck / Bus |
| Alcohol_Involved | Yes / No |
| Overspeeding_Severity | Yes / No / High |
| Drunk_Driving_Severity | Yes / No / High |

---

