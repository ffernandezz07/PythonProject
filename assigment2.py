import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel("Data Manipulation Worksheet.exe", sheet_name ="Financing Table Clean", parse_dates=['DATE'], index_col=['DATE'])
st.write(df)
