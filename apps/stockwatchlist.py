import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
import json
import requests  
from streamlit_lottie import st_lottie  
# Favicon and Page title 
from PIL import Image
img = Image.open('icon.png')
# Must be the first streamlit command
st.set_page_config(page_title="367-Hemant Saw", page_icon=img)
# icon8 credits
# <a target="_blank" href="https://icons8.com/icon/46034/australian-dollar">Australian Dollar</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

def app():
  st.markdown("____")    
  
  # URL lottie 
  def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
      return None
    return r.json()  


  # App title
  st.markdown('''
  # **🔰 Stock Watchlist 🔰**
  🔔 Shown are the Stock Price Data for search companies!

  **💎 Info**
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
  
  # Down Arrow Red
  lottie_downarrow = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_onm6cbny.json")
  st_lottie(
    lottie_downarrow,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    renderer="svg", # canvas
    height=150,
    width=700,
    key=None,
  ) 


  # Ticker data
  st.header('**🍀 Ticker data 🍀**')
  st.write(tickerDf)
  
  # Down Arrow Yellow
  lottie_downarrow = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_wuwif49b.json")
  st_lottie(
    lottie_downarrow,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    renderer="svg", # canvas
    height=150,
    width=700,
    key=None,
  ) 


  # Bollinger bands
  st.header('** 📈 Bollinger Bands 📉**')
  qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
  qf.add_bollinger_bands()
  fig = qf.iplot(asFigure=True)
  st.plotly_chart(fig)
  
  # Social links  
  st.subheader("")
  
  # Rocket
  lottie_rocket = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_88eq9kd8.json")
  connect_icon, connect_link = st.columns((0.05, 0.5))
  with connect_icon:
    st_lottie(lottie_rocket, height=60, key="rainbow")
  with connect_link:
    st.subheader("Connect With Me!")
  
  # Instagram
  lottie_instagram = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2ks3pjua.json")
  connect_icon, connect_link = st.columns((0.05, 0.5))
  with connect_icon:
    st_lottie(lottie_instagram, height=30, key="instagram")
  with connect_link:
    st.write("[Instagram](https://www.instagram.com/hemant_100_/)")

  # LinkedIn
  lottie_linkedIn = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_g7zwhgv2.json")
  connect_icon, connect_link = st.columns((0.05, 0.5))
  with connect_icon:
    st_lottie(lottie_linkedIn, height=30, key="linkedin")
  with connect_link:
    st.write("[LinkedIn](https://www.linkedin.com/in/hemant-saw-a122931b0/)")

  # Github
  lottie_github = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_SiFYir.json")
  connect_icon, connect_link = st.columns((0.05, 0.5))
  with connect_icon:
    st_lottie(lottie_github, height=25, key="github")
  with connect_link:
    st.write("[Github](https://github.com/hemantsaw100)")

  
  # lottie End Of Line 
  lottie_endline = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_vf7vzf32.json")
  st_lottie(
    lottie_endline,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    renderer="svg", # canvas
    height=250,
    width=700,
    key=None,
  )
  
  
  ####
  #st.write('---')
  #st.write(tickerData.info)
