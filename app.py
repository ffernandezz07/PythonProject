import pandas as pd
import streamlit as st

st.write("APP WORKING!")

tickers = ['AAPL','DIS','IBM']
ticker = st.selectbox("Pick a ticker", tickers)

df = pd.read_csv(ticker + '.csv', parse_dates=['Date'], index_col=['Date'])

begDate = df.index.min()
endDate = df.index.max()

pickStart = st.date_input("Pick start date:", begDate)
pickEnd = st.date_input("Pick end date:", endDate)


st.write(df.loc[pickStart:pickEnd])
st.write(begDate)
st.write(endDate)