import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
from PIL import Image
img = Image.open('favicon.png')
# Must be the first streamlit command
st.set_page_config(page_title="Stock Watchlist", page_icon=img)
# from multiapp import MultiApp
# from apps import crypto # import your app modules here

# app = MultiApp()

# App title
st.markdown('''
# Stock Watchlist
Shown are the stock price data for query companies!

**Info: **
- The Aim of the app is to provide an easy and simple way to search, visualize and analyze the S&P 500 companies (Standard And Poor)
with all the Up's and Down's in the Stock Market.
- Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Search')
start_date = st.sidebar.date_input("Start date", datetime.date(2015, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 8, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

# img = Image.open("stock.jpg")
# st.image(img)
# st.image("C:\Users\Hemant\Desktop\Web-Scrapping-Project\stock.png")

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

# Company full name
string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

# Zip code
zip_code = tickerData.info['zip']
st.header('Zip Code: **%r**' % zip_code)

# Sector
sector = tickerData.info['sector']
st.header('Sector: **%s**' % sector)

# State
state = tickerData.info['state']
st.header('State: **%s**' % state)

# Country
country = tickerData.info['country']
st.header('Country: **%s**' % country)

# Website Name
website_name = tickerData.info['website']
st.header('Website: **%s**' % website_name)

# st.write(tickerData.info)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)




# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)



# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)




####
#st.write('---')
#st.write(tickerData.info)

# For Multipage 

# Add all your application here
# app.add_app("avataar", avataar.app)
# app.add_app("crypto", crypto.app)

# The main app
# app.run()