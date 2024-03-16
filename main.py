import yfinance as yf
import streamlit as st

st.write("""
# Stock Price Visualizer

Shown below are the stock **closing price** and ***volume***!

""")

#set ticker
tickerSymbol = st.text_input("Ticker Symbol", "GOOGL")

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-3-16', end='2024-3-16')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)