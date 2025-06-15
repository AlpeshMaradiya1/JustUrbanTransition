# JustUrbanTransition
A Sample data-driven approach to identify climate-vulnerable communities in City using spatial, environmental, and socioeconomic indicators.

![JUT](https://github.com/user-attachments/assets/3700bfaf-5244-4258-8af0-d5681f1f1cd8)


🔍 Overview
This project develops a Just Transition Index (JTI) for City's municipal wards by integrating:

Air Quality Index (AQI)
Average Summer Temperature
Percentage of Slum Population
Green Cover per ward

It visualizes the findings using interactive maps and dashboards to identify communities most in need of green transitions. Inspired by Janagraha's Just Transition framework, this tool aims to support evidence-based policy planning for equitable climate resilience.

🧰 Tools & Technologies

Tool	Purpose
Python	Data cleaning, index computation
Pandas	Tabular data manipulation
NumPy	Normalization & statistical ops
Seaborn	Data visualization
GeoPandas	Spatial joins and mapping
Streamlit	Interactive web app

📊 Just Transition Index (JTI)

The JTI is a composite index built using normalized values of: JTI = (Normalized AQI + Temp + Slum Population + (1 - Green Cover)) / 4
(Higher JTI = Greater need for just transition interventions)
