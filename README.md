# Capstone Project: Energy Consumption Analytics for GreenPower Utilities

## Overview
This project aims to build an end-to-end data engineering and forecasting pipeline to help **GreenPower Utilities** analyze energy consumption patterns, forecast demand, and generate actionable insights using public energy and weather datasets.

## Project Structure

```
CAPSTONE-DATA/
│
├── code/
│   ├── Week2_data_clean_n_preprocess.ipynb
│   ├── Week3_data_ingestion_pipeline.ipynb
│   ├── Week4_feature_engineering.ipynb
│   ├── Week5_forecasting_models.ipynb
│   └── Week6_main.py
│
├── intermediate_files/
│   ├── arima_model_forecast.csv
│   ├── cleaned_combined_data_2007.csv
│   ├── energy_timeseries.db
│   ├── feature_table_daily.csv
│   └── feature_table_hourly.csv
│
├── raw_data/Data-weather-paris/
│   ├── paris 2007-01-01 to 2007-01-31.csv
│   ├── ...
│   └── paris 2007-12-01 to 2007-12-31.csv
│
└── Topic_5_Capstone Projects - Google Docs.pdf
```

## Features Implemented

### Week 2 – Data Cleaning
- Removed outliers, imputed missing timestamps, and aligned time intervals.

### 🔹 Week 3 – Data Ingestion Pipeline
- Automated scripts for ingesting weather and energy data into SQLite.

### 🔹 Week 4 – Feature Engineering
- Created aggregated features like hourly/daily consumption, peak-to-average ratios, etc.

### 🔹 Week 5 – Forecasting
- Built and evaluated time-series models like **ARIMA** to forecast energy demand.

### 🔹 Week 6 – Finalization
- Visualization.
- Dashboards planned using Streamlit.

## Datasets Used
- Weather data (2007, Paris) – `.csv` files in `raw_data/`
- Cleaned and transformed datasets – `intermediate_files/`
- Public sources: [OpenWeatherMap](https://openweathermap.org/), [UCI Power Consumption](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption)

## Technologies & Tools
- Python, Pandas, NumPy, Matplotlib, Plotly
- SQLite 
- Collab
- Git, GitHub, VS Code
- Streamlit

## Running the Project
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run main script:
   ```bash
   python code/Week6_main.py
   ```
