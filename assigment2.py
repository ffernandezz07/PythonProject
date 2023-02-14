import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel("Data Manipulation Worksheet.xlsx", sheet_name ="Financing Table Clean", engine='openpyxl')
st.write(df)
