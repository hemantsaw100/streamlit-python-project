import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
from PIL import Image
img = Image.open('favicon.png')
# Must be the first streamlit command
st.set_page_config(page_title="Stock Watchlist", page_icon=img)


# Navbar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000;">
  <a class="navbar-brand" href="#" style="color: #FF7777;">Stock watchlist</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="binance.py" target="_blank">Binance</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



# App title
st.markdown('''
# **🔰 Stock Watchlist 🔰**
Shown are the stock price data for query companies!

**Info 💎**
- The Aim of the app is to provide an easy and simple way to search, visualize and analyze the S&P 500 companies (Standard And Poor)
with all the Up's and Down's in the company with the help of a bolllinger band and a brief information about the company.
- Built in `Python` using libraries like `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Search 🔍')
start_date = st.sidebar.date_input("Start date 📆", datetime.date(2015, 1, 1))
end_date = st.sidebar.date_input("End date 📆", datetime.date(2021, 8, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker ⌛', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker


# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

# Company full name
string_name = tickerData.info['longName']
st.header('**☛ %s ☚**' % string_name)

# Sector
sector = tickerData.info['sector']
st.write('🚀 Sector: **%s**' % sector)

# State
state = tickerData.info['state']
st.write('📍 State: **%s**' % state)

# Country
country = tickerData.info['country']
st.write('🌏 Country: **%s**' % country)

# Zip code
zip_code = tickerData.info['zip']
st.write('🎯 Zip Code: **%r**' % zip_code)

# Website Name
website_name = tickerData.info['website']
st.write('💻 Website: **%s**' % website_name)

# st.write(tickerData.info)

string_summary = tickerData.info['longBusinessSummary']
st.subheader('🔥 About Company:')
st.info(string_summary)


# Ticker data
st.header('**🍀 Ticker data 🍀**')
st.write(tickerDf)


# Bollinger bands
st.header('** 📈 Bollinger Bands 📉**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)


####
#st.write('---')
#st.write(tickerData.info)
