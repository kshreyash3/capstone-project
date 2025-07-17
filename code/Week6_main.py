import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page setup ---
st.set_page_config(page_title="Energy Forecast Dashboard", layout="wide")

# --- Load the data ---
@st.cache_data
def load_data():
    df = pd.read_csv("arima_model_forecast.csv", parse_dates=["datetime"])
    return df

df = load_data()

# --- Sidebar: Date filter ---
st.sidebar.header("📅 Date Filter")
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["datetime"].min(), df["datetime"].max()]
)

start_date, end_date = pd.to_datetime(date_range)
df = df[(df["datetime"] >= start_date) & (df["datetime"] <= end_date)]

# --- Dashboard title ---
st.title("📊 Energy Consumption Forecasting Dashboard")

# --- Forecast vs Actual plot ---
st.subheader("🔍 Forecast vs Actual")
fig1 = px.line(
    df, x="datetime", y=["consumption", "forecast"],
    labels={"value": "Energy (kWh)", "variable": "Type"},
    title="Actual vs Forecasted Energy Consumption",
    markers=True
)
st.plotly_chart(fig1, use_container_width=True)

# --- Consumption trend plot ---
st.subheader("📈 Consumption Trend Over Time")
fig2 = px.line(
    df, x="datetime", y="consumption",
    labels={"consumption": "Energy (kWh)"},
    title="Energy Consumption Trend",
    markers=True
)
st.plotly_chart(fig2, use_container_width=True)

# --- Recommendations ---
st.subheader("📌 Final Recommendations for Operational Changes")
st.markdown("""
- 🔁 **Load Shifting**: Move heavy loads to off-peak hours (low consumption forecast).
- 🧠 **Model Feedback Loop**: Periodically retrain the ARIMA model to adapt to recent trends.
- 🚨 **Forecast Deviation Alerts**: If actual consumption differs from forecast by more than 10%, trigger alerts.
- 📆 **Predictive Scheduling**: Use forecast data for better operational planning and energy cost reduction.
""")
