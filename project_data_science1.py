import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# Stock Price App

Shows the stock price of Google! :chart_with_upwards_trend
""")

tikersymbol = 'GOOGL'

tikerData = yf.Ticker(tikersymbol)

tikerDf = tikerData.history(start='2010-5-31', end='2020-5-31')

st.line_chart(tikerDf.Close)
st.line_chart(tikerDf.Volume)