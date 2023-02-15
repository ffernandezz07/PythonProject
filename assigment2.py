import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel("Data Manipulation Worksheet.xlsx", sheet_name ="Financing Table Clean", parse_dates=['DATE'])
df.set_index(['DATE'], inplace=True)

st.title('Financial Deals Data through Plotly Graphs')
st.write('Total Deal Value by Type by Industry')

chart_type = ["Bar", "Box & Whisker", "Sunburst","Three Map"]
x_names = list(df.columns.values) 


st.sidebar.radio("Pick a chart type", options=chart_type)
st.sidebar.selectbox("Pick a category for the x-axis", options=x_names)