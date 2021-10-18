import streamlit as st
import pandas as pd
import json
import requests  
from streamlit_lottie import st_lottie


def app():
    # Inline CSS
    st.markdown(""" <style> 
                .font {
                    font-size:18px ; 
                    font-family: 'Alternate Gothic, Open Sans, sans-serif';
                    color: #FFEBA1;}
                # .underline {color: #FF0000} 
                </style> """, unsafe_allow_html=True)
    
    
    st.markdown("____")    

    st.markdown('''# ** ₿ Binance Price App ₿**
    ''')
    
    st.write('💎 A Simple Cryptocurrency price app pulling price data from Binance API')
        
    st.markdown('<p class="font"> 💰 Fun Fact: There are currently more than 65,000 cryptocurrency are in existence.</p>', unsafe_allow_html=True)

    st.header('**❄ Selected Price**')

    # Load market data from Binance API
    df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')


    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    col1, col2, col3 = st.columns(3)

    # Start of binance price in navbar
    st.sidebar.info('💲 Binance Coin Prices :')
    
    # Widget (Cryptocurrency selection box)
    col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
    col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
    col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )
    col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD') )
    col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
    col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
    col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
    col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('DOTBUSD') )
    col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD') )

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]
    col2_df = df[df.symbol == col2_selection]
    col3_df = df[df.symbol == col3_selection]
    col4_df = df[df.symbol == col4_selection]
    col5_df = df[df.symbol == col5_selection]
    col6_df = df[df.symbol == col6_selection]
    col7_df = df[df.symbol == col7_selection]
    col8_df = df[df.symbol == col8_selection]
    col9_df = df[df.symbol == col9_selection]

    # Apply a custom function to conditionally round values
    col1_price = round_value(col1_df.weightedAvgPrice)
    col2_price = round_value(col2_df.weightedAvgPrice)
    col3_price = round_value(col3_df.weightedAvgPrice)
    col4_price = round_value(col4_df.weightedAvgPrice)
    col5_price = round_value(col5_df.weightedAvgPrice)
    col6_price = round_value(col6_df.weightedAvgPrice)
    col7_price = round_value(col7_df.weightedAvgPrice)
    col8_price = round_value(col8_df.weightedAvgPrice)
    col9_price = round_value(col9_df.weightedAvgPrice)

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    col2_percent = f'{float(col2_df.priceChangePercent)}%'
    col3_percent = f'{float(col3_df.priceChangePercent)}%'
    col4_percent = f'{float(col4_df.priceChangePercent)}%'
    col5_percent = f'{float(col5_df.priceChangePercent)}%'
    col6_percent = f'{float(col6_df.priceChangePercent)}%'
    col7_percent = f'{float(col7_df.priceChangePercent)}%'
    col8_percent = f'{float(col8_df.priceChangePercent)}%'
    col9_percent = f'{float(col9_df.priceChangePercent)}%'

    # Create a metrics price box
    col1.metric(col1_selection, col1_price, col1_percent)
    col2.metric(col2_selection, col2_price, col2_percent)
    col3.metric(col3_selection, col3_price, col3_percent)
    col1.metric(col4_selection, col4_price, col4_percent)
    col2.metric(col5_selection, col5_price, col5_percent)
    col3.metric(col6_selection, col6_price, col6_percent)
    col1.metric(col7_selection, col7_price, col7_percent)
    col2.metric(col8_selection, col8_price, col8_percent)
    col3.metric(col9_selection, col9_price, col9_percent)
    
    # URL lottie 
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_cryptocurrency = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_yc9ywdm7.json") 
    st_lottie(
        lottie_cryptocurrency,
        speed=1,
        reverse=False,
        loop=True,
        quality="high", # medium ; high
        renderer="svg", # canvas
        height=500,
        width=700,
        key=None,
    )

    st.header('**🌈 All Price**')
    st.dataframe(df)
    
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

    st.markdown("""
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)
