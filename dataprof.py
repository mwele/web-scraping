import pandas as pd 
import yfinance as yf 
import streamlit as st 
st.write('''#Simple Stock App''')

tickerSymbol='GOOGL'

tickerData=yf.Ticker(tickerSymbol)

tickerDf=tickerData.history(period='id',start='2010-5-31',end='2020-5-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)