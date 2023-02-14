import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel("ExData\Data Manipulation Worksheet.xlsx", sheet_name ="Financing Table Clean", parse_dates=['DATE'])
df.set_index(['DATE'], inplace=True)
