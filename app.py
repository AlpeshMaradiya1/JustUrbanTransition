import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

# Load Data
geojson_path = r"\data\sample_wards.geojson"
csv_path = r"\data\delhi_jti_sample.csv"

gdf = gpd.read_file(geojson_path)
df = pd.read_csv(csv_path)

# Merge on Ward name ---
merged = gdf.merge(df, on="Ward")

# --- Normalize and calculate JTI ---
merged["JTI"] = (
    merged["AQI"] * 0.4 +
    (100 - merged["Green_Cover (%)"]) * 0.2 +
    merged["Avg_Temp (°C)"] * 0.2 +
    merged["Slum_Pop (%)"] * 0.2
)

# Normalize JTI between 0 and 1
min_val = merged["JTI"].min()
max_val = merged["JTI"].max()
merged["JTI_norm"] = (merged["JTI"] - min_val) / (max_val - min_val)

# Streamlit App 
st.set_page_config(layout="wide")
st.title("🌆 Just Transition Index (JTI) Across Delhi Sample Wards")

st.markdown("""
The **Just Transition Index (JTI)** represents how vulnerable each ward is in Delhi with respect to air quality, green cover, temperature, and slum population.  
Higher score = More vulnerable.
""")

# Plot using Plotly 
fig = px.choropleth_mapbox(
    merged,
    geojson=merged.geometry.__geo_interface__,
    locations=merged.index,
    color="JTI_norm",
    hover_name="Ward",
    hover_data={
        "AQI": True,
        "Green_Cover (%)": True,
        "Avg_Temp (°C)": True,
        "Slum_Pop (%)": True,
        "JTI_norm": ":.2f"
    },
    color_continuous_scale="Reds",
    mapbox_style="carto-positron",
    center={"lat": 28.6139, "lon": 77.2090},
    zoom=9,
    height=700
)

fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
st.plotly_chart(fig, use_container_width=True)