import streamlit as st
import pandas as pd
import numpy as np
import folium
import matplotlib.pyplot as plt
import plotly.express as px
from folium.plugins import HeatMap
from streamlit_folium import st_folium


st.set_page_config(page_title="My Project page",layout="wide")


st.title("🖥️My EDA Dashbord")
st.write("this dashbord contains survay layout.")



# Sidebar control

st.sidebar.header("control")
uploaded_file = st.sidebar.file_uploader(
    "Upload your CSV file", 
    type=["csv"], 
    key="csv_uploader_unique"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.sidebar.info("Upload a CSV file to unlock full dashboard features.")
    st.warning("⚠️ No dataset detected. Running with sample demo data.")

# Sample dataset
    
    np.random.seed(42)
    sample_size = 500

    df = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=sample_size, freq='D'),
        "City": np.random.choice(["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur"], size=sample_size),
        "Latitude": np.random.uniform(8.0, 12.5, size=sample_size),
        "Longitude": np.random.uniform(74.5, 77.5, size=sample_size),
        "Accident_Severity": np.random.choice(["Low", "Medium", "High"], size=sample_size),
        "Vehicle_Type": np.random.choice(["Car", "Bike", "Truck", "Bus"], size=sample_size),
        "Alcohol_Involved": np.random.choice(["Yes", "No"], size=sample_size),
        "Overspeeding_Severity": np.random.choice(["Yes", "No", "High"], size=sample_size),
        "Drunk_Driving_Severity": np.random.choice(["Yes", "No", "High"], size=sample_size),
    })

# Tabs

tab, tab01, tab0, tab1, tab2, tab3 = st.tabs(["📔Introduction","🛠️Tools","🗺️Map Visualization", "📊Data", "📈Visualization", "📝Summary"])

# Main tab

with tab:
    st.subheader("📎 PROJECT - INTRODUCTION")
    col1, col2 = st.columns(2)
    st.markdown("""
<style>
body {
    background: #0d1117;
    color: #e6edf3;
}

/* Title */
.title {
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    color: #8b949e;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Tabs */
.tabs {
    display: flex;
    gap: 30px;
    border-bottom: 1px solid #30363d;
    margin-bottom: 30px;
}
.tab {
    padding-bottom: 10px;
    cursor: pointer;
    color: #8b949e;
}
.tab.active {
    color: #ff4d4d;
    border-bottom: 2px solid #ff4d4d;
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 30px rgba(0,0,0,0.3);
}

/* Section Title */
.section-title {
    font-size: 26px;
    font-weight: 600;
    margin-bottom: 15px;
}

/* Bullet Points */
ul {
    line-height: 1.8;
    font-size: 16px;
}

.badge {
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
    color: white;
    padding: 6px 12px;
    border-radius: 20px;
    display: inline-block;
    font-size: 12px;
    font-weight: bold;

    box-shadow: 0 0 12px rgba(255,75,75,0.8);
}



</style>
""", unsafe_allow_html=True)
    
    st.markdown("""
<style>

/* 🔥 CARD STYLE (UPGRADED) */
.card {
    background: linear-gradient(135deg, #1f77b4, #00c6ff);
    padding: 25px;
    border-radius: 15px;
    color: white;

    /* ✨ Glow effect */
    box-shadow: 0 0 20px rgba(0,198,255,0.6);

    /* Smooth animation */
    transition: all 0.3s ease-in-out;
}

/* 🚀 HOVER EFFECT */
.card:hover {
    transform: translateY(-8px) scale(1.04);

    /* Stronger glow on hover */
    box-shadow: 0 0 40px rgba(0,198,255,0.9);
}



/* 🎯 TITLE */
.section-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* 📋 LIST */
ul {
    list-style: none;
    padding-left: 0;
}

li {
    margin-bottom: 8px;
    padding-left: 20px;
    position: relative;
}

/* 🔴 GLOWING BULLETS */
li::before {
    content: "";
    color: #ff4b4b;
    position: absolute;
    left: 0;

    /* Glow effect for bullet */
    text-shadow: 0 0 8px #ff4b4b;
}

</style>
""", unsafe_allow_html=True)
    
    




    # Column 1
    with col1:
    
        st.markdown("""
    <div class="card">
        <div class="badge">Project Aim</div>
        <div class="section-title">🎯 Objective</div>
        <ul>
            <li>Analyze accident risk patterns</li>
            <li>Visualize accident severity insights</li>
            <li>Build an easy-to-use dashboard</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Column 2
    with col2:
        st.markdown("""
    <div class="card">
        <div class="badge">Key Features</div>
        <div class="section-title">⚡ Highlights</div>
        <ul>
            <li>Interactive visualizations</li>
            <li>Real-time data exploration</li>
            <li>User-friendly interface</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
        st.markdown("### 📊 Quick Insights")

    c1, c2, c3 = st.columns(3)

    c1.markdown('<div class="card"><h3>🚗 1,245</h3><p>Total Accidents</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>⚠️ 320</h3><p>High Severity</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card"><h3>📉 12%</h3><p>Alcohol Cases</p></div>', unsafe_allow_html=True) 

#tool tab

with tab01:
    st.title("🔧Tools used in this Project")
    st.markdown("""
<div class="card">
 <div class="badge">Tools Used</div>
 <div class="section-title"> Main Tools</div>
 <ul>
     <li>Python</li>
     <li>----------</li>
     <li>Pandas</li>
     <li>Numpy<?li>
     <li>Folium</li>
     <li>Streamlit</li>
     
 </ul>
</div>
""",unsafe_allow_html=True)

#tab_0
    
with tab0:
    st.title("🚦 Accident Prone Area Analysis - Kerala")

#  Data Cleaning

    
    df.columns = df.columns.str.strip()

    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
    df = df.dropna(subset=["Latitude", "Longitude"])

    if "Overspee ding_Severity" in df.columns:
        df.rename(columns={"Overspee ding_Severity": "Overspeeding_Severity"}, inplace=True)

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    
# Filters


    st.sidebar.header("Filters")

    district = st.sidebar.multiselect("District", sorted(df["City"].dropna().unique()))
    severity = st.sidebar.multiselect("Severity", df["Accident_Severity"].dropna().unique())
    vehicle = st.sidebar.multiselect("Vehicle Type", df["Vehicle_Type"].dropna().unique())

    if district:
        df = df[df["City"].isin(district)]
    if severity:
        df = df[df["Accident_Severity"].isin(severity)]
    if vehicle:
        df = df[df["Vehicle_Type"].isin(vehicle)]

    
#  Date Filter


    min_date = df['Date'].min().date()
    max_date = df['Date'].max().date()

    date_range = st.sidebar.slider(
        "Select Date Range",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date)
    )

    df = df[(df['Date'].dt.date >= date_range[0]) &
            (df['Date'].dt.date <= date_range[1])]

    if df.empty:
        st.warning("No data available for selected filters")
        st.stop()

# Weight


    def calculate_weight(row):
        weight = 1
        if row["Accident_Severity"] == "High":
            weight += 3
        elif row["Accident_Severity"] == "Medium":
            weight += 2
        else:
            weight += 1
        if row["Alcohol_Involved"] == "Yes":
            weight += 2
        if str(row.get("Overspeeding_Severity", "")).lower() in ["high", "yes"]:
            weight += 2
        if str(row.get("Drunk_Driving_Severity", "")).lower() in ["high", "yes"]:
            weight += 2
        return weight

    df["weight"] = df.apply(calculate_weight, axis=1)

#️ Map


    center_lat = df["Latitude"].mean()
    center_lon = df["Longitude"].mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

    heat_data = df[["Latitude", "Longitude", "weight"]].values.tolist()
    HeatMap(heat_data, radius=15, blur=10).add_to(m)

    for _, row in df.sample(min(200, len(df)), random_state=42).iterrows():
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=3,
            popup=f"{row['City']} - {row['Accident_Severity']}",
            color="red",
            fill=True
        ).add_to(m)

    st.subheader("🔥 Accident Hotspot Heatmap")
    st_folium(m, width=1000, height=600)


# Insights


    st.subheader("📊 Insights")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Accidents", len(df))
    col2.metric("High Severity", len(df[df["Accident_Severity"] == "High"]))
    col3.metric("Alcohol Cases", len(df[df["Alcohol_Involved"] == "Yes"]))


    

#TAB_1
    
with tab1:
    st.subheader("Data Preview")
    st.dataframe(df)            

#TAB_2
    

with tab2:
    st.title("Detailed ")
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

    if numeric_columns:
        selected_col = st.sidebar.selectbox("Select column to visualize", numeric_columns)
        chart_type = st.sidebar.radio("Choose chart type", ["Line", "Bar", "Area"])         

        col1, col2 = st.columns([2, 1])               

        with col1:  # Left side for chart
            if chart_type == "Line":
                st.line_chart(df[selected_col])

            elif chart_type == "Bar":
                st.bar_chart(df[selected_col])

            elif chart_type == "Area":
                st.area_chart(df[selected_col])

                                
            else:
                st.warning("No 'severity' column found for pie chart.")

        with col2:  
            st.write("### Column Summary")
            st.write(df[selected_col].describe())

    else:
        st.warning("No numeric columns available for visualization.")
#TAB_3: Sunmary
                
with tab3:
    st.subheader(" Statiscical Summary")
    st.write(df.describe())
    csv = df.to_csv(index=False)
    st.download_button("⬇️ Download Filtered Data", csv, "filtered_data.csv")


