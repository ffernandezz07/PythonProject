import pandas as pd
import streamlit as st

st.write("APP WORKING!")

tickers = ['AAPL','DIS','IBM']
ticker = st.selectbox("Pick a ticker", tickers)

df = pd.read_csv(ticker + '.csv', parse_dates=['Date'], index_col=['Date'])

begDate = df.index.min()
endDate = df.index.max()

pickStart = st.date_input("Pick start date:", begDate, min_value=begDate)
pickEnd = st.date_input("Pick end date:", endDate)

filterDF = df.loc[pickStart:pickEnd] #keep the filter version of table as new variable
st.write(filterDF)

#P3 Lessons floder - copy codes to create chaers
import plotly.express as px
fig = px.line(filterDF.index, y= "Close")
st.plotly_chart(fig)


st.write(begDate)
st.write(endDate)