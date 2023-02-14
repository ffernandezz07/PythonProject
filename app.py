import pandas as pd
import streamlit as st

st.write("APP WORKING!")

tickers = ['AAPL','MSFT','NFLX']
st.selectbox("Pick a ticker", tickers)